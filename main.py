from customer import Customer
from services import TaxiService, BikeService, ScooterService, RollerbladesService, BusService

if __name__ == "__main__":
    customer = Customer("Jan")

    taxi_service = TaxiService()
    customer.order_transport(taxi_service)
    print("-" * 30)

    bike_service = BikeService()
    customer.order_transport(bike_service)
    print("-" * 30)

    scooter_service = ScooterService()
    scooter_service.available = False 
    customer.order_transport(scooter_service)
    print("-" * 30)

    rollerblades_service = RollerbladesService()
    customer.order_transport(rollerblades_service)
    print("-" * 30)

    bus_service = BusService()
    customer.order_transport(bus_service)
    print("-" * 30)