import time


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("username").click()
        wd.find_element_by_name("username").clear()
        wd.find_element_by_name("username").send_keys(username)
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()
        time.sleep(1)

    def is_login_open(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Logout"))

    def is_loggin_in_as(self,username):
        return self.get_user_loggin() == "%s" % username

    def get_user_loggin(self):
        wd = self.app.wd
        return  wd.find_element_by_css_selector("td.login-info-left span").text

    def login_ensure(self, username, password):
        if self.is_login_open() > 0:
            if self.is_loggin_in_as(username):
                return

            self.logout()
            self.login(username, password)
        self.app.open_home_page()
        self.login(username, password)

    def logout_ensure(self):
        if self.is_login_open() > 0:
            self.logout()
