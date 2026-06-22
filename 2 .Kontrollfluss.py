# --- if / elif /else ---
alter = 20

if alter < 13: 
    print("Kind")
elif alter  < 18:
    print("Jugendlicher")
else:
    print("Erwachsener")
    
 #--- Logische Operatoren in Bedingungen ---
temparatur = 25
ist_sonnig = True
if temparatur > 20 and ist_sonnig:
    print("Perfektes Wetter!")
if temparatur < 0 or temparatur > 35:
    print("Scheiß Wetter")

#--- while-Schleife ---
zaeler = 1

while zaeler <= 3:
    print("Hallo")
    zaeler += 1

# --- for-schleife (mit range)()) ---
for zaehler in range(5):  #0,1,2,3,4
    print("Zähler ist:", zaehler)

# --- range() mit Start, Ende und Schrittweite
for zaehler in range(2, 11, 2):   #2, 4, 6, 8, 10
    print("Gerade zahl:", zaehler)

    # --- for-Schleife mit String (Text) (und anderen sachen aber nicht jetzt) ---
    for buchstabe in "Hallo":
        print(buchstabe)

# --- break: Schleife vorzeiting abbrechen ---
for buchstabe in "Hallo":
    if buchstabe == "l":
        break
    print(buchstabe)
# --- continue: aktuellen Durchlauf überspringen ---
for i in range(5):
    if i == 2:
        continue   # überspringt nur die 2
    print("i ist:", i) # gibt also an: i ist 0/1/3/4