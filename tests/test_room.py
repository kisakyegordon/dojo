from unittest import TestCase


class RoomTests(TestCase):
    def setUp(self):
        self.room = Room()
        self.name = "blue"
        self.room_type = "office"

        self.room = Room(self, name, room_type)

    def test_check_room_instance(self):
        self.assetTrue(isinstance(self.room, Room))







