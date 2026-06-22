from Skill import Skill
from Pokemon import Pokemon
import random
import copy
# Pikachu setzt Donnerblitz ein. Das Ziel ist Palkia.

#----------------------------------------------------------------------------------------------
pikachu_skills = [Skill("Donnerblitz", 90, 85,"Elektro"),Skill("Donner", 110, 70,"Elektro"),Skill("Ruckzuckhieb", 40, 100, "Normal")]

pikachu = Pokemon("Pikachu", random.randint(211,304), pikachu_skills, "Elektro")

mabula_skills = [Skill("Käferbiss", 60 , 100, "Käfer"),Skill("Kreuzschere", 80, 80, "Käfer"),Skill("Schaufler", 90, 76,"Boden")]

mabula = Pokemon("Mabula",random.randint(154,298) , mabula_skills, "Käfer")

lorblatt_skills = [Skill("Solarstrahl", 120 , 65, "Planze"),Skill("Gigasauger", 75, 85, "Planze"),Skill("Rasierblatt", 55, 95, "Planze")]

lorblatt = Pokemon("Lorblatt", random.randint(230,304),lorblatt_skills, "Planze")

groudon_skills = [Skill("Eruption", 150 , 50,"Feuer"),Skill("Feuersturm", 110, 65, "Feuer"),Skill("Erdkräfte", 90, 77, "Boden")]

groudon = Pokemon("Groudon", random.randint(341,404),groudon_skills, "Feuer")

#+ wasser element pokemon

pk_list1 = [pikachu,mabula,lorblatt,groudon]
pk_list2 = copy.deepcopy(pk_list1)
#--------------------------------------------------------------------------------------------

pokemon1 = pk_list1[random.randint(0,len(pk_list1)-1)]
pokemon2 = pk_list2[random.randint(0,len(pk_list2)-1)]

print(f"Spieler 1 hat das Pokemon {pokemon1.name} bekommen")
print(f"Spieler 2 hat das Pokemon {pokemon2.name} bekommen")
print()
print()

while pokemon1.leben > 0 and pokemon2.leben > 0:
    print(f"{pokemon1.name} ({pokemon1.leben} HP) {pokemon1.element}")
    for i in range(len(pokemon1.skills)):
        print(f"{i}. {pokemon1.skills[i].name} {pokemon1.skills[i].schaden} Dmg {pokemon1.skills[i].genauigkeit}% {pokemon1.skills[i].element}")
    print()    
    skill_nr = int(input("Wähle ein Skill aus: "))
    print()
    pokemon1.use_skill(skill_nr, pokemon2)

    if pokemon2.leben <= 0:
        print("Spieler 1 Gewinnt")
        break




    print(f"{pokemon2.name} ({pokemon2.leben} HP) {pokemon2.element}")
    for i in range(len(pokemon2.skills)):
        print(f"{i}. {pokemon2.skills[i].name} {pokemon2.skills[i].schaden} Dmg {pokemon2.skills[i].genauigkeit}% {pokemon2.skills[i].element}")
    print()    
    skill_nr = int(input("Wähle ein Skill aus: "))
    print()
    pokemon2.use_skill(skill_nr, pokemon1)

    if pokemon1.leben <= 0:
        print("Spieler 2 Gewinnt")
        break




