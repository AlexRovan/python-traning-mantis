import enum
import os.path

class Status(enum.Enum):

    development = 10
    release = 30
    stable = 50
    obsolete = 70



def test (param):
    if not isinstance(param, Status):
        print("1")
    else:
        print("2")
    print(param.value)

#test(10)

