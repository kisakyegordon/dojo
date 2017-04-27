from modules.room import Room


class LivingSpace(Room):
    def __init__(self, name):
        self.capacity == 4

        super(LivingSpace, self).__init__(name)