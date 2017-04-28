class Person(object):
    

    def __init__(self, person_id, firstname, lastname, position=''):
        self.person_id = person_id
        self.firstname = firstname
        self.lastname = lastname
        self.position = position
        self.full_name = self.firstname + " " + self.lastname


class Fellow(Person):

    def __init__(self, *args, **kwargs):
        super(Fellow, self).__init__(*args, position = 'F')


class Staff(Person):

    def __init__(self, *args, **kwargs):
        super(Staff, self).__init__(*args, position = 'S')
