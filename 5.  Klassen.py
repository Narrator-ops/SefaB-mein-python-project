# --- Klassen definieren ---
class Hund:
    
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter

    def bellen(self):
        print(f"{self.name} sagt: Wuff !")
    
    def info(self):
        print(f"{self.name} ist {self.alter} Jahre alt")
  



hund1 = Hund("Max", 8)
hund2 = Hund("Jakob", 5)

hund1.bellen()
hund1.info()
hund2.info()
hund2.bellen()

print(hund1.alter)

hund1.alter += 3
hund1.info()

# --- Vererbung ---
class Saeugetier:

    def __init__(self, name, alter):
        self.name = name
        self.alter = alter
    
    def atmen(self):
        print("Atmen")

class Mensch(Saeugetier):

    def __init__(self, name ,alter ,geschlecht):
        super().__init__(name, alter)
        self.geschlecht = geschlecht
    
    def sprechen(self):
        print(f"hallo ich bin {self.name}")
    

sefa = Mensch("Sefa", 16 ,"Männlich")
sefa.atmen()

katze = Saeugetier("Sapsik", 4)

katze.atmen()
sefa.sprechen()
