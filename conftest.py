import pytest
from selenium import webdriver
from py.xml import html
BASE_URL = "https://www.youku.com"

_driver = None


def pytest_addoption(parser):
    """添加命令行--browser"""
    parser.addoption(
        "--browser", action="store", default="firefox", help="browser option:firefox or chrome"
    )


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """测试失败自动截图到HTML报告"""
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call" or report.when == "setup":
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_")+".png"
            screen_img = _capture_screenshot()
            if file_name:
                html = f'<div><img src="data:image/png;base64,{screen_img}" alt="screenshot" style="width:<px;height:200px" onclick="window.open(this.src) align="right"/></div>'
                extra.append(pytest_html.extras.html(html))
        report.extra = extra
        report.description = str(item.function.__doc__)
        report.nodeid = report.nodeid.encode("utf-8").decode("unicode_escape")


@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    """删除原有的Test列，插入Description和Test_nodeid列"""
    cells.insert(1, html.th("Description"))
    cells.insert(2, html.th("Test_nodeid"))
    cells.pop(2)


@pytest.mark.optionalhook
def pytest_html_results_table_rows(report, cells):
    """删除原有的Test列，插入Description和Test_nodeid列的详情"""
    cells.insert(1, html.td(report.description))
    cells.insert(2, html.td(report.nodeid))
    cells.pop(2)


def _capture_screenshot():
    return _driver.get_screenshot_as_base64()


@pytest.fixture(scope="session")
def driver(request):
    global _driver
    if _driver is None:
        name = request.config.getoption("--browser")
        if name.caplization() == "Firefox":
            _driver = webdriver.Firefox()
        elif name.caplization() == "Chrome":
            _driver = webdriver.Chrome()
        else:
            _driver = webdriver.Firefox()
    def fn():
        _driver.quit()
    request.addfinalizer(fn)
    return _driver
