from telnetlib import Telnet

class JamesHelper:

    def __init__(self, app):
        self.app = app

    def ensure_user_exsists(self,username,password):
        james_config = self.app.config
        session = JamesHelper.Session(james_config["james"]["host"],
                                      james_config["james"]["port"],
                                      james_config["james"]["username"],
                                      james_config["james"]["password"])
        if session.is_user_exsists(username):
            session.set_password_user(username,password)
        else:
            session.create_user(username,password)
        session.quit()

    class Session:

        def __init__(self,host,port,username,password):
            self.timeout = 5
            self.telnet = Telnet(host,port,self.timeout)
            self.read_until("Login id")
            self.write(username+'\n')
            self.read_until("Password")
            self.write(password+'\n')
            self.read_until("Welcome %s. HELP for a list of commands" % username)

        def read_until(self, text):
            self.telnet.read_until(text.encode('ascii'), self.timeout)

        def write(self,text):
            self.telnet.write(text.encode('ascii'))

        def create_user(self,user,pwd):
            self.write("adduser %s %s \n" % (user,pwd))
            self.read_until("User %s added" % user)

        def is_user_exsists(self,user):
            self.write("verify %s \n" % user)
            res = self.telnet.expect([b"exists",b"does not exist"],self.timeout)
            return res[0] == 0

        def set_password_user(self,user,pwd):
            self.write("setpassword %s %s \n" % (user,pwd))
            self.read_until("Password for %s reset" % user)

        def quit(self):
            self.write("quit")