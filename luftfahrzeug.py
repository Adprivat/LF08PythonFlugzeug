from abc import ABC, abstractmethod

class Luftfahrzeug(ABC):
    def __init__(self, bezeichnung: str, gewicht: float, baujahr: int):
        self.__bezeichnung = bezeichnung
        self.__gewicht = gewicht
        self.__baujahr = baujahr
    
    # Getter und Setter mit Datenkapselung
    def getBezeichnung(self) -> str:
        return self.__bezeichnung
    
    def setBezeichnung(self, bezeichnung: str) -> None:
        self.__bezeichnung = bezeichnung
    
    def getGewicht(self) -> float:
        return self.__gewicht
    
    def setGewicht(self, gewicht: float) -> None:
        self.__gewicht = gewicht
    
    def getBaujahr(self) -> int:
        return self.__baujahr
    
    def setBaujahr(self, baujahr: int) -> None:
        self.__baujahr = baujahr
    
    @abstractmethod
    def getDaten(self) -> str:
        pass

class Flugzeug(Luftfahrzeug):
    def __init__(self, bezeichnung: str, gewicht: float, baujahr: int, spannweite: float, anzahl_motoren: int):
        super().__init__(bezeichnung, gewicht, baujahr)
        self.__spannweite = spannweite
        self.__anzahl_motoren = anzahl_motoren
    
    def getSpannweite(self) -> float:
        return self.__spannweite
    
    def setSpannweite(self, spannweite: float) -> None:
        self.__spannweite = spannweite
    
    def getAnzahlMotoren(self) -> int:
        return self.__anzahl_motoren
    
    def setAnzahlMotoren(self, anzahl: int) -> None:
        self.__anzahl_motoren = anzahl
    
    def getDaten(self) -> str:
        return f"""
Flugzeug Details:
Bezeichnung: {self.getBezeichnung()}
Gewicht: {self.getGewicht()} kg
Baujahr: {self.getBaujahr()}
Spannweite: {self.getSpannweite()} m
Anzahl Motoren: {self.getAnzahlMotoren()}
"""

class Heissluftballon(Luftfahrzeug):
    def __init__(self, bezeichnung: str, gewicht: float, baujahr: int, ballonvolumen: float, korbhoehe: float):
        super().__init__(bezeichnung, gewicht, baujahr)
        self.__ballonvolumen = ballonvolumen
        self.__korbhoehe = korbhoehe
    
    def getBallonVolumen(self) -> float:
        return self.__ballonvolumen
    
    def setBallonVolumen(self, volumen: float) -> None:
        self.__ballonvolumen = volumen
    
    def getKorbhoehe(self) -> float:
        return self.__korbhoehe
    
    def setKorbhoehe(self, hoehe: float) -> None:
        self.__korbhoehe = hoehe
    
    def getDaten(self) -> str:
        return f"""
Heißluftballon Details:
Bezeichnung: {self.getBezeichnung()}
Gewicht: {self.getGewicht()} kg
Baujahr: {self.getBaujahr()}
Ballonvolumen: {self.getBallonVolumen()} m³
Korbhöhe: {self.getKorbhoehe()} m
""" 