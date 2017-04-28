from .person import *
from .room import *
import random


class Dojo(object):
    all_rooms = {}
    staff = []
    fellows = []
    staff_and_fellows = {}
    unallocated_people = {}
    office_rooms = defaultdict(list)
    living_space_rooms = defaultdict(list)

    @staticmethod
    def create_room(room_type, room_name):
        '''
        Check that the room does not exist and determine what type of room it is

        '''

        for room_name in room_name:
            # room_name=name_of_room[0]
            if room_name in Dojo.all_rooms:
                print('Room already exists')
                return 'Room already exists'
            elif room_type == 'office':

                current_room = Office(room_name)
                Dojo.all_rooms[current_room.room_name.upper()] = current_room.room_type
                Dojo.office_rooms[current_room.room_name.upper()]

                print('Office called %s created succesfully' % room_name)

            elif room_type == 'livingspace':
                current_room = LivingSpace(room_name)
                Dojo.all_rooms[current_room.room_name.upper()] = current_room.room_type
                Dojo.living_space_rooms[current_room.room_name.upper()]
                print('Living space called %s created succesfully' % room_name)

