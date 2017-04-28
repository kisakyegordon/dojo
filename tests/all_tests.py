import unittest
from unittest import TestCase
from models.dojo import Dojo
import unittest.mock as mock
import os
from collections import defaultdict


class TestDojo(TestCase):
    def test_create_office(self):
        previous_room_count = len(Dojo.all_rooms)
        self.assertFalse('blue_office' in Dojo.all_rooms)
        Dojo.create_room('office', 'blue_office')
        self.assertTrue('blue_office'.upper() in Dojo.all_rooms)
        new_room_count = len(Dojo.all_rooms)
        self.assertEqual(previous_room_count + 1, new_room_count)

    def test_create_ls(self):
        previous_room_count = len(Dojo.all_rooms)
        self.assertFalse('mutesa' in Dojo.all_rooms)
        Dojo.create_room('livingspace', 'mutesa')
        self.assertTrue('mutesa'.upper() in Dojo.all_rooms)
        new_room_count = len(Dojo.all_rooms)
        self.assertEqual(previous_room_count + 1, new_room_count)

    def test_room_does_not_exist(self):
        Dojo.create_room('office', 'blue_office')
        self.assertTrue('blue_office' in Dojo.all_rooms)
        response = Dojo.create_room('office', 'blue_office')
        self.assertEqual(response, "Room already exists")
