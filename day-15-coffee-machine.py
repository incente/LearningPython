guthaben = 0
menu = [{"name": "espresso",
         "preis": 1.5,
         "wasser": 50,
         "kaffee": 20,
         "milch": 0},
         {"name": "cappuccino",
          "preis": 2.5,
          "wasser": 50,
          "kaffee": 20,
          "milch": 50},
          {"name": "latte",
          "preis": 3,
          "wasser": 50,
          "kaffee": 20,
          "milch": 70}]
vorrat = {"wasser": 500,
          "kaffee": 200,
          "milch": 300}


def update_guthaben():
    global guthaben

    while True:
        try:
            eingegebener_betrag = float(input("Betrag einwerfen: 0.5, 1, 2 (0 = Beenden)\n"))

            guthaben += eingegebener_betrag
            print("Guthaben:",guthaben)

            if eingegebener_betrag == 0:
                break
        
        except ValueError:
            print("Das ist kein Geld Homie")


def kaffee_waehlen():
    global menu
    
    try:
        wahl = str(input("Kaffee waehlen: Espresso, Cappuccino, Latte\n")).lower()
            
        for kaffee in menu:
            if kaffee["name"] == wahl:
                return kaffee
    
    except ValueError:
        print("Dieser Kaffee ist nicht auf unserem Menü Homie")


def vergleich(wahl):
    global guthaben
    global vorrat

    if wahl["preis"] > guthaben:
        print("Zu wenig Guthaben", guthaben, "€")
        start()
    else:
        if wahl["wasser"] > vorrat["wasser"]:
            print("Zu wenig Wasser für:", wahl["name"], vorrat["wasser"], "/", wahl["wasser"], "ml")
            start()
        elif wahl["kaffee"] > vorrat["kaffee"]:
            print("Zu wenig Kaffee für:", wahl["name"], vorrat["kaffee"], "/", wahl["kaffee"], "g")
            start()
        elif wahl["milch"] > vorrat["milch"]:
            print("Zu wenig Milch für:", wahl["name"], vorrat["milch"], "/", wahl["milch"], "ml")
            start()
        else:
            output(wahl)


def output(wahl):
    global guthaben

    rueckgeld = guthaben - wahl["preis"]

    print("Hier ist dein", wahl["name"], "und dein Rückgeld:", rueckgeld, "€")



def start():
    update_guthaben()
    vergleich(kaffee_waehlen())

start()