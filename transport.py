"""
Moduł transport.py
------------------
Zawiera definicje klas reprezentujących konkretne produkty (pojazdy)
w strukturze wzorca projektowego Factory Method (Metoda Fabrykująca).
"""

from abc import ABC, abstractmethod

class Transport(ABC):
    """
    Klasa abstrakcyjna definiująca interfejs dla wszystkich rodzajów transportu.
    Określa wspólne zachowania, które musi zaimplementować każdy pojazd.
    """
    @abstractmethod
    def vehicle_type(self):
        """Zwraca nazwę/typ pojazdu."""
        pass

    @abstractmethod
    def arrival_time(self):
        """Zwraca przewidywany czas przyjazdu pojazdu do klienta."""
        pass

    @abstractmethod
    def travel_time(self):
        """Zwraca przewidywany czas trwania podróży."""
        pass

class Taxi(Transport):
    """Klasa reprezentująca transport typu Taxi."""
    def vehicle_type(self):
        return "Taxi"

    def arrival_time(self):
        return "7 minutes"

    def travel_time(self):
        return "10 minutes"

class Bike(Transport):
    """Klasa reprezentująca transport typu Bike (Rower)."""
    def vehicle_type(self):
        return "Bike"

    def arrival_time(self):
        return "3 minutes"

    def travel_time(self):
        return "20 minutes"

class Scooter(Transport):
    """Klasa reprezentująca transport typu Scooter (Hulajnoga)."""
    def vehicle_type(self):
        return "Scooter"

    def arrival_time(self):
        return "2 minutes"

    def travel_time(self):
        return "15 minutes"