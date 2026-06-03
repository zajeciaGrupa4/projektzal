"""
Moduł main.py
-------------
Główny plik uruchomieniowy aplikacji, prezentujący przykładowe działanie programu,
weryfikację działania wzorca Factory Method oraz mechanizm blokowania dostępności pojazdów.
"""

from customer import Customer
from services import TaxiService, BikeService, ScooterService

if __name__ == "__main__":
    # Tworzenie obiektu klienta
    customer = Customer("Jan")

    # Przykład 1: Zamówienie usługi Taxi
    taxi_service = TaxiService()
    customer.order_transport(taxi_service)
    print("-" * 30)

    # Przykład 2: Zamówienie usługi Bike
    bike_service = BikeService()
    customer.order_transport(bike_service)
    print("-" * 30)

    # Przykład 3: Próba zamówienia niedostępnej usługi Scooter
    scooter_service = ScooterService()
    scooter_service.available = False 
    customer.order_transport(scooter_service)