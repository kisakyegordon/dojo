import random
from room import LivingSpace, Office
from person import Fellow, Staff


class Dojo(object):
    def __init__(self):
        self.all_rooms = []
        self.empty_rooms = []
        self.offices = []
        self.empty_offices = []
        self.livingspaces = []
        self.empty_livingspaces = []
        self.initial_room_count = 0
        self.staffs = []
        self.fellows = []
        self.all_people = []
        self.unallocated_person = []

    def create_room(self, room_type, *args):
        """Check that the room does not exist and determine what type of room it is"""
        print(args)
        for rname in args:

            if rname not in [room.room_name for room in self.all_rooms]:
                # Create Room
                print ("Creating room")
                new_room = Office(room_type,rname) if room_type == "office" else LivingSpace(room_type,rname)
                self.all_rooms.append(new_room)

            else:
                print ("Room with name {0} already exists".format(rname))
        # new_rooms = []
        # for room in args["<room_name>"]:
        #     if room.lower() in [k.room_name.lower() for k in self.all_rooms]:
        #         print ("Already exists!")
        #         return
        #
        # if args["<room_type>"] == "Office":
        #     new_room = Office(room)
        #     self.offices.append(new_room)
        #
        # elif args["<room_type>"] == Living:
        #     new_room = Living(room)
        #     self.livingspaces.append(new_room)
        #
        # self.all_rooms.append(new_room)
        # new_rooms.append(new_room)




class Calculator(object):
    def add(self, x, y):
        return x + y