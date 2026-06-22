# --- Liste ---
einfkaufsliste = ["Milch","Brot","Eier"]
#in einer Liste können auch integer, Floats, Booleans etc. stehen

print(einfkaufsliste[0])     # erstes Element: Milch
print(einfkaufsliste[2])     # drittes  Element: Eier
print(einfkaufsliste[-1])    # leztes Element: Eier

einfkaufsliste.append("Butter")     # hinten hinzufügen
# Milch, Brot, Eier, Butter
einfkaufsliste.remove("Eier")       # Element wird entfernt
# Milch, Brot, Butter
einfkaufsliste[1] = "Mehl"          # Element ändern
# Milch, Mehl, Butter

print(len(einfkaufsliste))
print(einfkaufsliste)

# --- Dictionary --
person = {"name": "Sefa", "alter":16, "stadt": "Darmstadt"}

print(person["name"])
person["alter"] = 18
person["Lieblingsanime"] = "Gurren Lagann"

print(person)

#--- Schleife mit einer Liste ---
for artikel in einfkaufsliste:
    print(f"{artikel} x 2")


# --- Schleife mit einer Dictionary ---
for schuessel, wert in person.items():
    print(f"{schuessel}:{wert}")

# --- Verschachtelung ---
spielerliste = [
    {"name": "Emre", "score": 30, "items":[]},
    {"name": "Sefa", "score": 50, "items":["Schwert"]},
    {"name": "Mina", "score": 100, "items":["AK47", "Panzer"]},
    {"name": "Enes", "score": 99, "items":["revolver", "f-16"]},
]

for spieler in spielerliste :
    print(f"{spieler["name"]} hat dise items {spieler["items"]} und hat ein score von {spieler["score"]}")