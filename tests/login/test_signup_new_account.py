import string
import random


def random_string(prefix,maxlen = 10):
    symbols = string.ascii_letters
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def test_signup_new_account(app):
    user = random_string("user")
    pwd = 'test'
    email = user + '@localhost'
    app.james.ensure_user_exsists(user,pwd)
    app.signup.signup_new_account(user,email,pwd)
    app.session.login(user,pwd)
    assert app.soap.can_login("administrator","root")
    app.session.logout_ensure()