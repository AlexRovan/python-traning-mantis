import poplib
import email
import time

class EmailHelper:

    def __init__(self, app):
        self.app = app

    def get_email (self,usename,password,subject):
        for i in range(5):
            pop = poplib.POP3(self.app.config["james"]["host"])
            pop.user(usename)
            pop.pass_(password)
            count = pop.stat()[0]
            if count > 0:
                for n in range(count):
                    msglines = pop.retr(n+1)[1]
                    msgtext = '\n'.join(map(lambda x: x.decode('utf-8'),msglines))
                    msg = email.message_from_string(msgtext)
                    if msg.get("Subject") == subject:
                        pop.dele(n+1)
                        pop.quit()
                        return msg.get_payload()
            pop.quit()
            time.sleep(3)
        return None