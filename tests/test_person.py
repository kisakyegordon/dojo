from unittest import TestCase
from modules.person import Person


class TestPerson(TestCase):
    def setUp(self):
        self.name = "gordon kisakye"
        self.person = Person(self.name)

    def test_name_type(self):
        self.assertIsInstance(self.name, str, msg="Enter string")

