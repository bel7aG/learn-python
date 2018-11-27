class Owner:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def ohLaLa(self, pLanguage):
        return "{} sings {}".format(self.name, pLanguage)

    def danceHoHo():
        return "{} is now Dancing"


bel7aG = Owner("Belhassen", "Gharsallah", 21)
bel7aGOhLaLa = bel7aG.ohLaLa('Javascript')
print(bel7aGOhLaLa)
