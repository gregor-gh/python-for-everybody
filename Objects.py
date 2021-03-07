class PartyAnimal:
    x = 0
    name = ""

    def __init__(self, z):  # constructor
        self.name = z
        print(self.name, "constructed")

    def party(self):  # self reference to current instance of class, does not have to be self
        self.x = self.x + 1
        print("So far", self.x)

    def __del__(self):  # destructor, seldom used
        print("I am destructed", self.x)


an = PartyAnimal("Sally")

an.party()
an.party()
an.party()

# print(dir(an))
# print(type(an))

# inheritance


class FootballFan(PartyAnimal):  # footballfan extends partyanimal
    points = 0

    def touchdown(self):
        self.points += 7
        self.party()
        print(self.name, "points", self.points)


bob = FootballFan("Bob")

bob.touchdown()
bob.touchdown()
