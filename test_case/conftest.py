import pytest
from page_object.login import *

@pytest.fixture(scope="session",autouse=True)
def login(driver):
    _login(driver,user="18268878747",psw="Qaz123456!")