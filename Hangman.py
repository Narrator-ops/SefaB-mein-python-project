from Clear import clear

leben = 11
hangman = {  
        11 : "",
        10 : "/",
        9  : "/\\" ,
        8  : "  | \n  | \n  | \n  | \n  | \n /\\" ,
        7  : "  ________ \n  | \n  | \n  | \n  | \n  | \n /\\" ,
        6  : "  ________ \n  |       | \n  | \n  | \n  | \n  | \n /\\" ,
        5  : "  ________ \n  |       | \n  |       O \n  | \n  | \n  | \n /\\" ,
        4  : "  ________ \n  |       | \n  |       O \n  |       | \n  | \n  | \n /\\" ,
        3  : "  ________ \n  |       | \n  |       O \n  |       | \n  |      / \n  | \n /\\" ,
        2  : "  ________ \n  |       | \n  |       O \n  |       | \n  |      / \\ \n  | \n /\\" ,
        1  : "  ________ \n  |       | \n  |      \\O \n  |       | \n  |      / \\ \n  | \n /\\" ,
        0  : "  ________ \n  |       | \n  |      \\O/\n  |       | \n  |      / \\ \n  | \n /\\" ,
}
spiel_zuende = False



# Wort auswählen
wort = input("Wähle ein Wort aus (nur Kleinbuchstaben) ")
clear()
wortlaenge = len(wort)
unfertiges_wort =[]
for i in range(wortlaenge):  #0,1,2,3,4,.....wortlaenge-1
        unfertiges_wort.append("_")

while spiel_zuende == False:
    print(unfertiges_wort)

    # Man darf zwischen Buchstaben oder Wort auswählen
    # option = input("Willst du das Wort schätzen ?[y/n] ")
    # if option == "y":
    #     wort_geschaetzt = input("Wort: ")
    #     if wort_geschaetzt == wort:
    #         print(f"Du hast Gewonnen ! Das Wort war {wort}")
    #         spiel_zuende = True
    #     else :
    #         print(f"Du hast falsch geraten. Du hast verloren ! Das Wort war {wort}")
    #         print(hangman[0])
    #         spiel_zuende = True

    # elif option == "n":
    buchstabe_geschaetzt = input("Buchstabe: ")
    if buchstabe_geschaetzt in wort:
        print("Richtig erraten !")
        for position in range(wortlaenge):
            if wort[position] == buchstabe_geschaetzt:
                unfertiges_wort[position] = buchstabe_geschaetzt
        if not "_" in unfertiges_wort:
            print(f"Du hast Gewonnen ! Das Wort war {wort}")
            spiel_zuende = True
    else:
        print("Falsch geraten !")
        leben -= 1
        print(hangman[leben])
        if leben == 0 :
            print(f" Du hast verloren ! Das Wort war {wort}")
            spiel_zuende = True


    
