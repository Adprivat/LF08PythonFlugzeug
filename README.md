Luftfahrzeug-Verwaltungsprogramm
==========================================

1. Einführung
-------------
In diesem Programm lernst du, wie ein objektorientiertes Verwaltungssystem für Luftfahrzeuge funktioniert. Du wirst sehen, wie die wichtigsten Konzepte der objektorientierten Programmierung (OOP) in der Praxis umgesetzt werden. Das Programm ermöglicht dir die Verwaltung von Flugzeugen und Heißluftballons über ein benutzerfreundliches Menüsystem.

2. Objektorientierte Konzepte
----------------------------
Im Programm findest du vier grundlegende OOP-Konzepte:

a) Abstraktion:
   - Die abstrakte Basisklasse 'Luftfahrzeug' gibt die Grundstruktur vor
   - Schau dir an, wie die abstrakte Methode definiert wird:
     ```python
     from abc import ABC, abstractmethod
     
     class Luftfahrzeug(ABC):
         @abstractmethod
         def getDaten(self) -> str:
             pass
     ```
   - Diese Methode muss von allen Kindklassen implementiert werden

b) Vererbung:
   - Deine Klassen 'Flugzeug' und 'Heissluftballon' erben von 'Luftfahrzeug'
   - Hier ein Beispiel für die Vererbung:
     ```python
     class Flugzeug(Luftfahrzeug):
         def __init__(self, bezeichnung: str, gewicht: float, baujahr: int, spannweite: float, anzahl_motoren: int):
             super().__init__(bezeichnung, gewicht, baujahr)
             self.__spannweite = spannweite
             self.__anzahl_motoren = anzahl_motoren
     ```

c) Datenkapselung:
   - Du schützt deine Daten durch private Variablen (mit '__' Prefix)
   - Der Zugriff erfolgt nur über Getter und Setter:
     ```python
     def getBezeichnung(self) -> str:
         return self.__bezeichnung
     
     def setBezeichnung(self, bezeichnung: str) -> None:
         self.__bezeichnung = bezeichnung
     ```

d) Polymorphismus:
   - Jede deiner Kindklassen implementiert getDaten() anders:
     ```python
     # In der Flugzeug-Klasse:
     def getDaten(self) -> str:
         return f"""
         Flugzeug Details:
         Bezeichnung: {self.getBezeichnung()}
         Gewicht: {self.getGewicht()} kg
         """
     
     # In der Heissluftballon-Klasse:
     def getDaten(self) -> str:
         return f"""
         Heißluftballon Details:
         Bezeichnung: {self.getBezeichnung()}
         Ballonvolumen: {self.getBallonVolumen()} m³
         """
     ```

3. Programmstruktur
------------------
Dein Programm besteht aus zwei Hauptdateien:

a) luftfahrzeug.py:
   - Hier findest du die Klassendefinitionen
   - Ein Beispiel für die Grundstruktur:
     ```python
     from abc import ABC, abstractmethod
     
     class Luftfahrzeug(ABC):
         # ... (wie oben gezeigt)
     
     class Flugzeug(Luftfahrzeug):
         # ... (wie oben gezeigt)
     ```

b) main.py:
   - Hier ist die Verwaltungslogik und das Menüsystem
   - Beispiel für die Menüstruktur:
     ```python
     class LuftfahrzeugVerwaltung:
         def menu(self):
             while True:
                 print("\n=== Luftfahrzeug Verwaltung ===")
                 print("1. Neues Flugzeug erstellen")
                 print("2. Neuen Heißluftballon erstellen")
                 # ...
     ```

4. Funktionalitäten
------------------
Das sind deine Hauptfunktionen:

a) Standardobjekte:
   - Beim Start werden automatisch zwei Beispiele erstellt:
     ```python
     def standardobjekte_erstellen(self):
         standard_flugzeug = Flugzeug(
             bezeichnung="Airbus A320",
             gewicht=42000.0,
             baujahr=2020,
             spannweite=35.8,
             anzahl_motoren=2
         )
         self.luftfahrzeuge.append(standard_flugzeug)
     ```

b) Menüoptionen:
   1. Neues Flugzeug erstellen:
      ```python
      def flugzeug_erstellen(self):
          try:
              bezeichnung = input("Bezeichnung: ")
              gewicht = float(input("Gewicht (kg): "))
              # ...
          except ValueError:
              print("Fehler: Bitte gültige Werte eingeben!")
      ```

5. Fehlerbehandlung
------------------
So werden deine Eingaben geschützt:
```python
try:
    wahl = int(input("\nBitte wählen Sie eine Option (1-4): "))
    if wahl < 1 or wahl > 4:
        print("Ungültige Eingabe!")
except ValueError:
    print("Bitte eine Zahl eingeben!")
```

6. Verwendung des Programms
--------------------------
So startest du das Programm:

1. Öffne deine Kommandozeile
2. Navigiere in das Projektverzeichnis:
   ```bash
   cd pfad/zu/deinem/projekt
   ```
3. Starte das Programm:
   ```bash
   python main.py
   ```
4. Wähle im Menü die gewünschte Option
5. Folge den Anweisungen zur Eingabe
6. Bei Fehlern bekommst du hilfreiche Meldungen
7. Zum Beenden wählst du Option 4
