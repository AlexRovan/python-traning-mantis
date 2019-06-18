import random
from model.project import *

project_1 = Project(name="name_3",description="desx_3")

def test_add_project(app,db):
    if len(db.get_project_list()) == 0:
        app.project.create_new_project(project_1)
    old_project = db.get_project_list()
    project = random.choice(old_project)
    app.project.delete_project_by_id(project.id)
    old_project.remove(project)
    new_project = db.get_project_list()
    assert sorted(old_project,key=Project.id_or_max) == sorted(new_project,key=Project.id_or_max)