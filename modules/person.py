class Person(object):

    def __init__(self, name):

#        self.gender = gender
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError("name must be a string")

