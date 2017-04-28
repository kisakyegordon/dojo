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

    @staticmethod
    def add_person(firstname, lastname, position, wants_accomodation='N'):
        '''
        Add person details to the system
        '''
        full_name = firstname + " " + lastname
        person_id = len(list(Dojo.staff_and_fellows)) + 1

        if full_name.upper() in Dojo.staff_and_fellows:
            print ('Person %s already exists.' % full_name)

        elif position.upper() == 'F' and wants_accomodation.upper() == 'Y':
            new_fellow = Fellow(person_id, firstname, lastname)
            Dojo.staff_and_fellows[new_fellow.full_name.upper()] = position
            Dojo.fellows.append(new_fellow.full_name.upper())
            random_office = Dojo.generate_random_office()
            random_ls = Dojo.generate_random_living_space()
            if not random_office and not random_ls:
                Dojo.unallocated_people[new_fellow.full_name.upper()] = position
                print('Added %s to the unallocated list' % new_fellow.full_name)
            elif not random_office and random_ls:
                Dojo.unallocated_people[new_fellow.full_name.upper()] = position
                print('Added %s to the unallocated list' % new_fellow.full_name)
                Dojo.living_space_rooms[random_ls].append(new_fellow.full_name.upper())
                print("Added: %s and allocated them to a living space %s: " % (new_fellow.full_name, random_ls))
            elif not random_ls and random_office:
                Dojo.unallocated_people[new_fellow.full_name.upper()] = position
                print('Added %s to the unallocated list' % new_fellow.full_name)
                Dojo.office_rooms[random_office].append(new_fellow.full_name.upper())
                print("Added: %s and allocated them to an office %s: " % (new_fellow.full_name, random_office))

            else:
                Dojo.office_rooms[random_office].append(new_fellow.full_name.upper())
                print("Added: %s and allocated them to %s: " % (new_fellow.full_name, random_office))
                Dojo.living_space_rooms[random_ls].append(new_fellow.full_name.upper())
                print("Added: %s and allocated them to %s: " % (new_fellow.full_name, random_ls))

        elif position.upper() == 'F':
            new_fellow = Fellow(person_id, firstname, lastname)
            Dojo.staff_and_fellows[new_fellow.full_name.upper()] = position
            Dojo.fellows.append(new_fellow.full_name.upper())
            random_office = Dojo.generate_random_office()
            if not random_office:
                Dojo.unallocated_people[new_fellow.full_name.upper()] = position
                print('Added %s to the unallocated list' % new_fellow.full_name)
            else:
                Dojo.office_rooms[random_office].append(new_fellow.full_name.upper())
                print("Added: %s and allocated them to %s: " % (new_fellow.full_name, random_office))

        elif position.upper() == 'S' and wants_accomodation.upper() == 'Y':
            new_staff = Staff(person_id, firstname, lastname)
            Dojo.staff_and_fellows[new_staff.full_name.upper()] = position
            Dojo.staff.append(new_staff.full_name)
            random_office = Dojo.generate_random_office()
            if not random_office:
                Dojo.unallocated_people[new_staff.full_name.upper()] = position
                print('Added %s to the unallocated list' % new_staff.full_name)
                print('Staff cannot be llocated a living space')
            else:
                Dojo.office_rooms[random_office].append(new_staff.full_name.upper())
                print("Added: %s and allocated them to %s: " % (new_staff.full_name, random_office))
                print('Staff cannot be llocated a living space')

        elif position.upper() == 'S':
            new_staff = Staff(person_id, firstname, lastname)
            Dojo.staff_and_fellows[new_staff.full_name.upper()] = position
            Dojo.staff.append(new_staff.full_name.upper())
            random_office = Dojo.generate_random_office()
            if not random_office:
                Dojo.unallocated_people[new_staff.full_name.upper()] = position
                print('Added %s to the unallocated list' % new_staff.full_name)
            else:
                Dojo.office_rooms[random_office].append(new_staff.full_name.upper())
                print("Added: %s and allocated them to %s: " % (new_staff.full_name, random_office))

        else:
            print('%s is not a valid position.' % position)

    @staticmethod
    def load_people(filename):
        '''
        Loads people to the system from a text file.
        '''
        if filename:
            with open(filename) as people_file:
                for line in people_file:
                    people_details = line.split()
                    if len(people_details) == 4:
                        Dojo.add_person(firstname=people_details[0], lastname=people_details[1],
                                        position=people_details[2], wants_accomodation=people_details[3])
                    elif len(people_details) == 3:
                        Dojo.add_person(firstname=people_details[0], lastname=people_details[1],
                                        position=people_details[2], wants_accomodation='N')
                    else:
                        print('Cannot process the data provided')
        else:
            print('Provide a file, please')