from unittest import TestCase
from modules.room import Room


class RoomTests(TestCase):
    def setUp(self):
        self.name = "blue"
        self.room_type = "OFFICE"
        self.room = Room(self.name, self.room_type)

    def test_check_room_instance(self):
        self.assertTrue(isinstance(self.room, Room))

    def test_room_attributes(self):
        self.assertEqual(self.room_type, self.room_type, msg="attributes not innitialised")
        self.assertEqual(self.room, self.room, msg="attributes  not innitialised")










