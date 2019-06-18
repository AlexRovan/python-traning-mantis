import sys
import enum


class Status(enum.Enum):

    development = 10
    release = 30
    stable = 50
    obsolete = 70


class View_status(enum.Enum):

    public = 10
    private = 50


class Project:

    def __init__(self, name = None, status = None, view_status = None, inhert = True, description = None, id = None):
        self.id = id
        self.name = name

        if not isinstance(status, Status):
            self.status = None
        else:
            self.status = status

        if not isinstance(view_status, View_status):
            self.view_status = None
        else:
            self.view_status = view_status

        self.inhert = inhert
        self.description = description

    def __repr__(self):
        return "Group: %s %s %s" % (self.id,self.name,self.description)

    def __eq__(self, other):
        return self.name == other.name and ( self.id == other.id or self.id is None or other.id is None)

    def id_or_max(self):
        if self.id is None:
            return sys.maxsize
        else:
            return int(self.id)
