from collections import defaultdict


class Room(object):

    """
    Models all the information of the rooms that the office and Living space will
    inherit from
    """

    def __init__(self, room_type, room_name, max_occupants=0):
        self.room_name = room_name
        self.room_type = room_type
        self.max_occupants = max_occupants


class Office(Room):

    def __init__(self, room_type, room_name, max_occupants=6):
        super(Office, self).__init__(room_type, room_name, max_occupants)

class LivingSpace(Room):

    def __init__(self, room_type, room_name, max_occupants=4):
        super(LivingSpace, self).__init__(room_type, room_name, max_occupants)


