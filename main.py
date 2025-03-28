from luftfahrzeug import Flugzeug, Heissluftballon

class LuftfahrzeugVerwaltung:
    def __init__(self):
        self.luftfahrzeuge = []
        # Standardobjekte erstellen
        self.standardobjekte_erstellen()

    def standardobjekte_erstellen(self):
        # Standardflugzeug erstellen
        standard_flugzeug = Flugzeug(
            bezeichnung="Airbus A320",
            gewicht=42000.0,
            baujahr=2020,
            spannweite=35.8,
            anzahl_motoren=2
        )
        self.luftfahrzeuge.append(standard_flugzeug)

        # Standard-Heißluftballon erstellen
        standard_ballon = Heissluftballon(
            bezeichnung="Cameron Z-Series",
            gewicht=250.0,
            baujahr=2021,
            ballonvolumen=2800.0,
            korbhoehe=1.2
        )
        self.luftfahrzeuge.append(standard_ballon)

    def menu(self):
        while True:
            print("\n=== Luftfahrzeug Verwaltung ===")
            print("1. Neues Flugzeug erstellen")
            print("2. Neuen Heißluftballon erstellen")
            print("3. Alle Luftfahrzeuge anzeigen")
            print("4. Programm beenden")
            
            try:
                wahl = int(input("\nBitte wählen Sie eine Option (1-4): "))
                
                if wahl == 1:
                    self.flugzeug_erstellen()
                elif wahl == 2:
                    self.heissluftballon_erstellen()
                elif wahl == 3:
                    self.alle_anzeigen()
                elif wahl == 4:
                    print("Programm wird beendet. Auf Wiedersehen!")
                    break
                else:
                    print("Ungültige Eingabe! Bitte wählen Sie eine Zahl zwischen 1 und 4.")
            except ValueError:
                print("Fehler: Bitte geben Sie eine gültige Zahl ein!")

    def flugzeug_erstellen(self):
        print("\n=== Neues Flugzeug ===")
        try:
            bezeichnung = input("Bezeichnung: ")
            gewicht = float(input("Gewicht (kg): "))
            baujahr = int(input("Baujahr: "))
            spannweite = float(input("Spannweite (m): "))
            anzahl_motoren = int(input("Anzahl Motoren: "))

            flugzeug = Flugzeug(bezeichnung, gewicht, baujahr, spannweite, anzahl_motoren)
            self.luftfahrzeuge.append(flugzeug)
            print("\nFlugzeug wurde erfolgreich erstellt!")
        except ValueError:
            print("Fehler: Bitte geben Sie gültige Werte ein!")

    def heissluftballon_erstellen(self):
        print("\n=== Neuer Heißluftballon ===")
        try:
            bezeichnung = input("Bezeichnung: ")
            gewicht = float(input("Gewicht (kg): "))
            baujahr = int(input("Baujahr: "))
            ballonvolumen = float(input("Ballonvolumen (m³): "))
            korbhoehe = float(input("Korbhöhe (m): "))

            ballon = Heissluftballon(bezeichnung, gewicht, baujahr, ballonvolumen, korbhoehe)
            self.luftfahrzeuge.append(ballon)
            print("\nHeißluftballon wurde erfolgreich erstellt!")
        except ValueError:
            print("Fehler: Bitte geben Sie gültige Werte ein!")

    def alle_anzeigen(self):
        if not self.luftfahrzeuge:
            print("\nKeine Luftfahrzeuge vorhanden!")
            return
        
        print("\n=== Alle Luftfahrzeuge ===")
        for i, luftfahrzeug in enumerate(self.luftfahrzeuge, 1):
            print(f"\nLuftfahrzeug {i}:")
            print(luftfahrzeug.getDaten())

if __name__ == "__main__":
    verwaltung = LuftfahrzeugVerwaltung()
    verwaltung.menu() 