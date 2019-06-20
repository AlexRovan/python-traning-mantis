

def test_session(app):
    assert app.soap.can_login("administrator","root")