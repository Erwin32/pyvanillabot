

class WowObject(object):

    def __init__(self, ObjectPointer):

        self.ObjectPointer = ObjectPointer

        self.Guid = self.get_guid()
        self.Descriptor = self.get_descriptor()
        self.Name = self.get_name()

        self.Location = self.get_location()
        self.Rotation = self.get_rotation()
        self.DistanceFromPlayer = self.get_dist_from_player()

    def get_guid(self):

    def get_descriptor(self):

    def get_name(self):
        """
        Method for obtaining name changes based on obj type.
        This must be overridden by subclass
        """
        return NotImplemented

    def get_location(self):

    def get_rotation(self):

    def get_dist_from_player(self):



