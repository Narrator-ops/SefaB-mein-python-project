from Clear import clear

s1_gewonnen = 0
s2_gewonnen = 0
s1_wahlliste = []
s2_wahlliste = []
runde = 1 


while s2_gewonnen != 2 or s1_gewonnen != 2 : # anfang, ende-1, schritte
    print("runde:", runde)
    runde += 1

    #Spieler 1 wählt zwischen Schere, Stein, Papier
    s1_wahl =input("Wähle zwischen Schere, Stein, Papier")
    s1_wahlliste.append(s1_wahl)
    clear()

    #Spieler 2 wählt zwischen Schere, Stein, Papier
    s2_wahl =input("Wähle zwischen Schere, Stein, Papier")
    s2_wahlliste.append(s2_wahl)
    clear()
   

    # Wer hat Gewonnen ? und den Gewiiner ausgeben
    # if s1_wahl == "Schere":
    #     if s2_wahl == "Schere":
    #         print("Unentschieden")
    #     elif s2_wahl == "Stein":
    #         print("Spieler 2 Gewinnt")
    #     elif s2_wahl == "Papier":
    #         print("Spieler 1 Gewonnen")
    # elif s1_wahl == "Stein":
    #     if s2_wahl == "Schere":
    #         print("Spieler 1 Gewonnen")
    #     elif s2_wahl == "Stein":
    #         print("Unentschieden")
    #     elif s2_wahl == "Papier":
    #         print("Spieler 2 Gewonnen")
    # elif s1_wahl == "Papier":
    #     if s2_wahl == "Schere":
    #         print("Spieler 2 Gewonnen")
    #     elif s2_wahl == "Stein":
    #         print("Spieler 1 Gewonnen")
    #     elif s2_wahl == "Papier":
    #         print("Unentschieden")

    if (s1_wahl == "Schere" and s2_wahl == "Papier") or (s1_wahl == "Stein" and s2_wahl == "Schere") or (s1_wahl == "Papier" and s2_wahl == "Stein"):
        print("Spieler 1 Gewonnen")
        s1_gewonnen += 1
    elif(s2_wahl == "Schere" and s1_wahl == "Papier") or (s2_wahl == "Stein" and s1_wahl == "Schere") or (s2_wahl == "Papier" and s1_wahl == "Stein"):
        print("Spieler 2 Gewonnen")
        s2_gewonnen += 1
    else:
        print("Unentschieden")
    
    if s2_gewonnen == 2 or s1_gewonnen == 2 :
        print("Spiel zuende")
        print(s1_wahlliste)
        print(s2_wahlliste)
        break 


