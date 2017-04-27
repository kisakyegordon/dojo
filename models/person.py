class Person(object):
    """
    Models the information of a person that the
    class Fellow and Staff will inherit from
    """

    def __init__(self, person_id, name, position=''):
        self.person_id = person_id
        self.name = name
        self.position = position


class Fellow(Person):

    def __init__(self, person_id, name, position='fellow'):
        super(Fellow, self).__init__(person_id, name, position)


class Staff(Person):

    def __init__(self, person_id, name, position='staff'):
        super(Staff, self).__init__(person_id, name, position)