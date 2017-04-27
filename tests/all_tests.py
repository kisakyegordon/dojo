import unittest
import os
import sys
import inspect
currentdir = os.path.dirname(os.path.abspath(
   inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from models.dojo import Dojo



class TestDojo(unittest.TestCase):

    def setUp(self):
        self.test_dojo = Dojo()

    # Test Room Creation
    def test_create_room(self):
        initial_room_count = len(self.test_dojo.all_rooms)
        blue_office = self.test_dojo.create_room("office", "blue")
        #self.assertTrue(blue_office, msg="not true")
        new_room_count = len(self.test_dojo.all_rooms)
        self.assertEqual(new_room_count - initial_room_count, 1)

    def test_create_living_space(self):
        self.test_dojo.create_room({
        "<room_type>": ["LivingSpace"],
        "Living": True,
        "Office": False
    })

    def test_create_office_space(self):
        self.test_dojo.create_room({
        "<room_type>": ["Office"],
        "Living": False,
        "Office": True
    })




if __name__ == '__main__':
    unittest.main()