from modules.room import Room


class OfficeSpace(Room):
    def __init__(self, name):
        self.capacity == 6

        super(Office, self).__init__(name)