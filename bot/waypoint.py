class WayPointType:
    Normal = 0
    Vendor = 1
    Repair = 2
    Ghost = 3
    Branch = 4
    NoType = 5

class WayPointCollection(list):

    def __init__(self):

    def __get__(self):

    def __set__(self):

class WayPoint(object):

    def __init__(self):
        self.ConnectedTo = None
        self.Location = None
        self.WayPointType = None

    def is_connected(self):
        return (self.ConnectedTo != None)

    def connected_type(self):
        if self.is_connected():
            return self.ConnectedTo.WayPointType
        else:
            return None

