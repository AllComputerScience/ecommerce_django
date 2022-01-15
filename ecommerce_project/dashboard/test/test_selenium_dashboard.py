# The file name must begin with test by default, but it can be in any directory.
# pytest.ini can be used to change the naming convention


import pytest

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

@pytest.mark.selenium
def test_create_new_admin_user(create_admin_user):
    assert create_admin_user.__str__() == 'superuser'

# To avoid transaction rollback, include the pytest fixture as a parameter. In this case; "create_admin_user"
@pytest.mark.selenium
def test_dashboard_admin_login(live_server, create_admin_user, chrome_browser_instance):

    browser = chrome_browser_instance
    browser.get(("%s%s" % (live_server.url, '/admin/login')))

    user_name = browser.find_element(By.NAME, 'username')
    user_password = browser.find_element(By.NAME, 'password')
    submit = browser.find_element(By.XPATH, '//input[@value="Log in"]')
    user_name.send_keys('superuser')
    user_password.send_keys('xyz')
    submit.send_keys(Keys.RETURN)

    assert 'Site administration' in browser.page_source