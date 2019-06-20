import re

class SignUpHelper:

    def __init__(self, app):
        self.app = app

    def signup_new_account(self,username,email,password):
        wd = self.app.wd
        wd.get(self.app.base_url)
        wd.find_element_by_link_text("Signup for a new account").click()
        wd.find_element_by_name("username").click()
        wd.find_element_by_name("username").send_keys(username)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").send_keys(email)
        wd.find_element_by_css_selector("input[type='submit']").click()

        mail = self.app.mail.get_email(username,password,"[MantisBT] Account registration")
        url = self.find_url_in_msg(mail)

        wd.get(url)
        wd.find_element_by_name("password").send_keys(password)
        wd.find_element_by_name("password_confirm").send_keys(password)
        wd.find_element_by_css_selector("input[value='Update User']").click()

    def find_url_in_msg(self,text):
        return re.search("http://.*$",text,re.MULTILINE).group(0)