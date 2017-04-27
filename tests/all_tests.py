import os
import sys
import inspect
import unittest
from models.dojo import Dojo
print os.path.abspath(__file__)
currentdir = os.path.dirname(os.path.abspath(
   inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)


class TestDojo(unittest.TestCase):

    def setUp(self):
        self.test_dojo = Dojo()

    def test_create_room(self):
            initial_room_count = len(self.test_dojo.all_rooms)
            blue_office = self.test_dojo.create_room("office", "blue")
            self.assertTrue(blue_office)
            new_room_count = len(self.test_dojo.all_rooms)
            self.assertEqual(new_room_count - initial_room_count, 1)

#     def test_room_created(self):
#        pass


if __name__ == '__main__':
    unittest.main()