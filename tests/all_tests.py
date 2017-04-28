import unittest
from unittest import TestCase
from models.dojo import Dojo
import unittest.mock as mock
import os
from collections import defaultdict


class TestDojo(TestCase):

    """ Create Room Tests """

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

        """ Person Tests  """

    def test_add_person_staff(self):
        Dojo.create_room('MARS', 'O')
        previous_staff_count = len(Dojo.staffs)
        self.assertFalse('KISAKYE GORDON' in Dojo.all_people)
        Dojo.add_person('KISAKYE', 'GORDON', 'S')
        self.assertTrue('KISAKYE GORDON' in Dojo.all_people)
        current_staff_count = len(Dojo.staffs)
        self.assertEqual(previous_staff_count + 1, current_staff_count, 'Person staff has not been added')

    def test_add_fellow(self):
        Dojo.create_room('MARS', 'O')
        previous_fellow_count = len(Dojo.fellows)
        self.assertFalse('NANYANZI IVY' in Dojo.all_people)
        Dojo.add_person('nanyanzi', 'ivy', 'F')
        self.assertTrue('NANYANZI IVY' in Dojo.all_people)
        current_fellow_count = len(Dojo.fellows)
        self.assertEqual(previous_fellow_count + 1, current_fellow_count, 'Person fellow has not been added')

        """ Random Room Tests """

    def test_return_random_office_room(self):
        Dojo.create_room('office', 'blue')
        Dojo.create_room('office', 'green')
        random_office = Dojo.generate_random_office()
        self.assertIn(random_office, Dojo.office_rooms)

    def test_return_random_ls_room(self):
        Dojo.create_room('livingspace', 'zebaki')
        Dojo.create_room('livingspace', 'pluto')
        random_ls = Dojo.generate_random_living_space()
        self.assertIn(random_ls, Dojo.living_space_rooms)

        """ Reallocation Tests """
    def test_reallocate_person(self):
        Dojo.create_room('livingspace', 'oregon')
        Dojo.create_room('office', 'makel')
        Dojo.add_person('joel', 'kanye', 'F', 'Y')
        self.assertIn('joel kanye', Dojo.living_space_rooms['oregon'])
        Dojo.create_room('GO', 'l')
        Dojo.reallocate_person_to_ls('Hesbon Laban', 'hela')
        self.assertIn('Hesbon Laban', Dojo.living_space_rooms['hela'])
        self.assertNotIn('Hesbon Laban', Dojo.living_space_rooms['oregon'])

    def test_does_not_reallocate_to_a_full_ls_room(self):
        Dojo.create_room('livingspace', 'oregon')
        Dojo.create_room('office', 'makel')
        previous_count = len(Dojo.living_space_rooms['oregon'])
        Dojo.add_person('hellen', 'degenerez', 'F', 'Y')
        Dojo.add_person('viona', 'awuor', 'F', 'Y')
        Dojo.add_person('patrice', 'leah', 'F', 'Y')
        Dojo.add_person('okindo', 'omutuka', 'F', 'Y')
        current_count = len(Dojo.living_space_rooms['oregon'])
        self.assertEqual(previous_count + 4, current_count)
        Dojo.create_room('livingspace', 'oregon')
        Dojo.add_person('anderson', 'masese', 'F', 'Y')
        response = Dojo.reallocate_person_to_ls('anderson masese', 'oregon')
        self.assertEqual(response, 'OREGON is already full')

    def test_does_reallocate_to_same_ls_room(self):
        Dojo.create_room('livingspace', 'oregon')
        Dojo.add_person('Mary', 'Mwenda', 'F', 'Y')
        response = Dojo.reallocate_person_to_ls('Mary Mwenda ', 'oregon')
        self.assertEqual(response, 'MARY MWENDA is already allocated to oregon')

    def test_does_not_reallocate_to_a_full_office_room(self):
        Dojo.create_room('office', 'blue')
        previous_count = len(Dojo.office_rooms['blue'])
        Dojo.add_person('degenez', 'hellen', 'F')
        Dojo.add_person('viona', 'awuor', 'F')
        Dojo.add_person('patrice', 'leah', 'S')
        Dojo.add_person('okindo', 'omutka', 'F')
        Dojo.add_person('liza', 'muli', 'S')
        Dojo.add_person('justin', 'Mzonge', 'S')
        current_count = len(Dojo.office_rooms['blue'])
        self.assertEqual(previous_count + 6, current_count)
        Dojo.create_room('office', 'guantanamo')
        Dojo.add_person('anderson', 'masese', 'F')
        response = Dojo.reallocate_person_to_office('anderson masese', 'blue')
        self.assertEqual(response, 'BLUE is already full')

    def test_does_reallocate_to_same_office_room(self):
        Dojo.create_room('office', 'blue')
        Dojo.add_person('mundi', 'james', 'F')
        response = Dojo.reallocate_person_to_office('mundi james', 'blue')
        self.assertEqual(response, 'MUNDI JAMES is already allocated to blue')

