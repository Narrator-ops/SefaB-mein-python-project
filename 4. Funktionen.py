# --- Einfaache Funktion ---
def begruessen():
    print("Hallo")

begruessen()

# --- Funktion mit Parameter ---
def begruesse_name(name):
    print(f"Hallo {name}")

begruesse_name("Sefa")
begruesse_name("Emre")

# --- Funktion mit Rückgabewert ---
def addiere(x,y):
    ergebnis = x + y
    return ergebnis

ergebnis = addiere(3,4)
print("Summe: ",addiere(2,2))
print("Summe: ",ergebnis)

# --- lokale vs globale Variable
nachricht = "global" 

def zeige_nachricht():
    nachricht = "lokal" 
    print("Nachricht: ", nachricht)

zeige_nachricht()
print("Nachricht: ", nachricht)
