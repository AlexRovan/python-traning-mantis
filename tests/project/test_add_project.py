from data.projects import *


def test_add_project(app):
    username = app.config["webadmin"]["username"]
    password = app.config["webadmin"]["password"]

    project = project_3
    old_project = app.soap.get_project_list(username,password)
    app.session.login_ensure(username,password)
    app.project.create_new_project(project)
    new_project = app.soap.get_project_list(username,password)
    old_project.append(project)
    assert sorted(old_project,key=Project.id_or_max) == sorted(new_project,key=Project.id_or_max)