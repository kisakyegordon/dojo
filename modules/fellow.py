from modules.person import Person


class Fellow(Person):
    def __init__(self, name, wants_living, gender=None ):

        yes = 'Y'
        no = 'N'
        male = 'M'
        female = 'F'

        if(wants_living == yes or wants_living == no):
            self.wants_living == wants_living
        else:
            raise ValueError("Entered value is incorrect, please use lower case")

        if(gender == male or gender == female):
            self.gender = gender
        else:
            raise ValueError("Entered gender value is incorrect")

        super(Fellow, self).__init__(name)