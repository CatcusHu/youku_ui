from lib.base import Base

"""元素定位1---登录"""
loc_to_user_login_path = ("css selector", ".navbtn")
loc_to_user_inputbox = ("css selector", ".user-input")
loc_to_psw_inputbox = ("css selector", ".psw-input")
loc_to_login_btn = ("css selector", ".login-btn")
loc_to_agree = ("css selector", ".protocol-agree")

"""元素定位2---用户登录断言"""
loc_username_path = ("css selector", "p.username")


def _login(driver, user, psw):
    mgtv = Base(driver)
    driver.get("https://www.youku.com")
    mgtv.click(loc_to_user_login_path)
    mgtv.send_words(loc_to_user_inputbox, user)
    mgtv.send_words(loc_to_psw_inputbox, psw)
    mgtv.click(loc_to_agree)
    mgtv.click(loc_to_login_btn)

# def login_success(derver,assert_text):
#     mgtv = Base(driver)
#     return mgtv.is_text_in_element(loc_username_path,assert_text)
