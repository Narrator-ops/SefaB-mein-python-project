import random


class Skill:

    def __init__(self, name, schaden, genauigkeit, element):
        self.name = name
        self.schaden = schaden
        self.genauigkeit = genauigkeit
        self.element = element 

    def use(self, ziel: Pokemon):
        if  random.randint(0,100) <= self.genauigkeit:
            # Stärker: Feuer > pflanze > Wasser > Feuer (dmg x 1,5)
            # Schwach: Feurer > Wasser > Planze > Feuer (dmg x 0,5)
            # Gleich: Feuer > Feuer (keing dmg)
            ziel.leben -= self.schaden
            print(f"{ziel.name} hat {self.schaden} Schaden bekommen.")
            print(f"{ziel.name} hat noch {ziel.leben} leben.")
            print()
        else :
            print(f"{self.name} ging daneben !")
            print()