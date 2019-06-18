from model.project import *
import string
import random

def random_string(prefix,maxlen = 10):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

project_1 = Project(name=random_string("name"),status=Status.release,inhert= True ,view_status=View_status.public,description="desx_1")
project_2 = Project(name=random_string("name"),status=Status.release,inhert= False ,view_status=View_status.public,description="desx_1")
project_3 = Project(name=random_string("name"),status=Status.obsolete,description="desx_1")
project_4 = Project(name=random_string("name"),description="desx_1")