

def test_session(app):
    assert app.session.is_loggin_in_as("administrator")