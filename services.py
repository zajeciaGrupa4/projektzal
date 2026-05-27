from abc import ABC, abstractmethod
from transport import Taxi, Bike, Scooter


class TransportServices(ABC):
    def __init__(self):
        self.available = True

    @abstractmethod
    def create_transport(self):
        pass

    @abstractmethod
    def transport_name(self):
        pass

    def order_transport(self):
        transport_object = self.create_transport()

        if self.available:
            print(f"Typ pojazdu: {transport_object.vehicle_type()}")
            print(f"Przewidywany czas przyjazdu: {transport_object.arrival_time()}")
            print(f"Przewidywany czas podróży: {transport_object.travel_time()}")
        else:
            print(f"Brak dostępnych pojazdów typu {self.transport_name()}.")


class TaxiService(TransportServices):
    def create_transport(self):
        return Taxi()

    def transport_name(self):
        return "Taxi"


class BikeService(TransportServices):
    def create_transport(self):
        return Bike()

    def transport_name(self):
        return "Bike"


class ScooterService(TransportServices):
    def create_transport(self):
        return Scooter()

    def transport_name(self):
        return "Scooter"