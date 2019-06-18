from data.projects import *


def test_add_project(app,db):
    project = project_3
    old_project = db.get_project_list()
    app.project.create_new_project(project)
    new_project = db.get_project_list()
    old_project.append(project)
    assert sorted(old_project,key=Project.id_or_max) == sorted(new_project,key=Project.id_or_max)