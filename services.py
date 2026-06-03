"""
Moduł services.py
-----------------
Zawiera klasy twórców (Creators) realizujące wzorzec Factory Method.
Odpowiada za logikę biznesową zamawiania transportu oraz zarządzanie jego dostępnością.
"""

from abc import ABC, abstractmethod
from transport import Taxi, Bike, Scooter

class TransportServices(ABC):
    """
    Abstrakcyjna klasa bazowa dla usług transportowych (Creator).
    Deklaruje metodę fabrykującą create_transport oraz zawiera główną logikę
    biznesową zamawiania pojazdów i weryfikacji ich dostępności.
    """
    def __init__(self):
        """Inicjalizuje usługę transportową jako domyślnie dostępną."""
        self.available = True

    @abstractmethod
    def create_transport(self):
        """
        Metoda fabrykująca (Factory Method).
        Musi zostać nadpisana przez podklasy w celu zwrócenia konkretnego obiektu Transport.
        """
        pass

    @abstractmethod
    def transport_name(self):
        """Zwraca tekstową nazwę usługi transportowej."""
        pass

    def order_transport(self):
        """
        Główna metoda realizująca zamówienie pojazdu.
        Sprawdza dostępność usługi. Jeśli jest dostępna, zamawia pojazd
        i zmienia jego status dostępności na False.
        """
        transport_object = self.create_transport()

        if self.available:
            print(f"Typ pojazdu: {transport_object.vehicle_type()}")
            print(f"Przewidywany czas przyjazdu: {transport_object.arrival_time()}")
            print(f"Przewidywany czas podróży: {transport_object.travel_time()}")
            self.available = False
            print(f"Pojazd {self.transport_name()} został zamówiony i jest teraz niedostępny.")
        else:
            print(f"Brak dostępnych pojazdów typu {self.transport_name()}.")

class TaxiService(TransportServices):
    """Konkretna usługa fabrykująca odpowiedzialna za tworzenie obiektów typu Taxi."""
    def create_transport(self):
        return Taxi()

    def transport_name(self):
        return "Taxi"

class BikeService(TransportServices):
    """Konkretna usługa fabrykująca odpowiedzialna za tworzenie obiektów typu Bike."""
    def create_transport(self):
        return Bike()

    def transport_name(self):
        return "Bike"

class ScooterService(TransportServices):
    """Konkretna usługa fabrykująca odpowiedzialna za tworzenie obiektów typu Scooter."""
    def create_transport(self):
        return Scooter()

    def transport_name(self):
        return "Scooter"