from suds.client import Client
from suds import WebFault
from model.project import *

class SoapHelper:

    def __init__(self,app):
        self.app = app

    def can_login(self,username,password):
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username,password)
            return True
        except WebFault:
            return False

    def get_project_list(self,username,password):
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        try:
            projects = client.service.mc_projects_get_user_accessible(username, password)
            return self.convert_project(projects)

        except WebFault:
            return None

    def convert_project(self,projects):
        def convert(projec):
            return Project(id=projec.id,
                           name=projec.name,
                           status=Status(int(projec.status.id)),
                           inhert=bool(projec.enabled),
                           view_status=View_status(int(projec.view_state.id)),
                           description=projec.description)

        return list(map(convert,projects))