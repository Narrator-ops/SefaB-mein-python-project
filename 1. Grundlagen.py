# - - - Variablen ---
name = "Sefa"  # String (Text)
alter = 16      # Interger (Ganzzahl)
groesse = 1.70  # Float (Kommazahlen)
ist_mann = True # Boolean (Wahr/Falsh) (True/False)

name2 ="Merve" 
alter2 = 28
groesse2 = 1.63
ist_mann2= False

#--- Ausgabe---
print("Name:", name)
print("Alter:", alter)
print("Größe:", groesse)
print("Mann:", ist_mann)

#---Eingabe (kommt immer aks String) ---
eingabe = input("Wie alt bist du ?")    #Alter steht als String (Text)

# --- Typumwandlung (Casting)--- 
eingabe_als_zahl = int(eingabe) #String (Text) -> Integer (Zahl)

print("Nächstes Jahr bist du", eingabe_als_zahl+1)

# --- Arithmetische Operatoren (Rechnen)---
print("Summe:", eingabe_als_zahl + 5)
print("Differenz:", eingabe_als_zahl - 5)
print("Produkt:", eingabe_als_zahl * 2)
print("Division:", eingabe_als_zahl / 2) # 10 / 3 = 3.33333333

print("Ganzzahl-Division:", eingabe_als_zahl // 3) #runden auf ne ganze Zahl 10 // 3 = 3
print("Rest (modulo):", eingabe_als_zahl % 3) # 10 % 3 = 1
print("Potenz:", eingabe_als_zahl ** 3) # 10 ** 3 = 10 * 10 * 10 = 1000

eingabe_als_zahl += 5 # eingabe_als_zahl = eingabe_als_zahl + 5
# +=, -=, /=, *=,...

print("Gleich + Operator:", eingabe_als_zahl )

#--- Vergleichsoperatoren (Ergebnis immer Boolean (Wahr/Falsch))---
print(eingabe_als_zahl < 30)
print(eingabe_als_zahl == 21)
print(eingabe_als_zahl != 21)
print(eingabe_als_zahl >= 13)

# --- Logische Operatoren (Ergebnis auch Boolean) ---
print(ist_mann and alter > 18)
print(ist_mann or alter > 90)
print(not ist_mann)

# --- String_Zusammensetzen (f-String)---
print(f"{name} ist {alter} Jahre alt.")