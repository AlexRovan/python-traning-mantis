import random
from model.project import *

project_1 = Project(name="name_3",description="desx_3")

def test_add_project(app):
    username = app.config["webadmin"]["username"]
    password =app.config["webadmin"]["password"]

    if len(app.soap.get_project_list(username,password)) == 0:
        app.project.create_new_project(project_1)
    old_project = app.soap.get_project_list(username,password)
    project = random.choice(old_project)
    app.session.login_ensure(username,password)
    app.project.delete_project_by_id(project.id)
    old_project.remove(project)
    new_project = app.soap.get_project_list(username,password)
    assert sorted(old_project,key=Project.id_or_max) == sorted(new_project,key=Project.id_or_max)