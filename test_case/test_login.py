import pytest
from page_object.login import _login


class TestLoginUser:
    @pytest.fixture(scope="function", autouse=True)
    def open(self, driver):
        driver.get("https://www.mgtv.com")
        driver.delete_all_cookies()
        driver.refresh()

    @pytest.mark.parametrize('user,psw', [(18268878747, "Qaz123456!"), (18267835018, "Qaz123456!")])
    def test_login(self, driver, user, psw):
        _login(driver, user, psw)


if __name__ == "__main__":
    pytest.main(["-s", "test_login.py"])
