from pony.orm import *
from model.project import *

class ORM_fixture:

    db = Database()

    def __init__(self,host,database,user,password):
        self.db.bind("mysql",host=host,database=database,user=user,password=password)
        self.db.generate_mapping()
        sql_debug(True)

    class ORM_Project(db.Entity):
        _table_='mantis_project_table'
        id = PrimaryKey(int, column ='id')
        name = Optional(str,column ='name')
        status = Optional(int,column ='status')
        view_status = Optional(int,column ='view_state')
        description = Optional(str, column='description')
        inherit_global = Optional(int, column='inherit_global')

    def convert_project(self,projects):
        def convert(projec):
            return Project(id=projec.id,
                           name=projec.name,
                           status=Status(projec.status),
                           inhert=bool(projec.inherit_global),
                           view_status=Status(projec.view_status),
                           description=projec.description)

        return list(map(convert,projects))

    @db_session
    def get_project_list(self):
        return self.convert_project(select(p for p in ORM_fixture.ORM_Project))



