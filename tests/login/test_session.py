

def test_session(app):
    app.session.login("administrator","root")
    assert app.session.is_loggin_in_as("administrator")