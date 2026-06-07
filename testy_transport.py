import unittest
from services import TaxiService, BikeService, ScooterService, RollerbladesService, BusService
from transport import Taxi, Bike, Scooter, Rollerblades, Bus

class TestTransportProject(unittest.TestCase):
    def test_taxi_service_creation_and_methods(self):
        service = TaxiService()
        transport_object = service.create_transport()
        self.assertIsInstance(transport_object, Taxi)
        self.assertEqual(transport_object.vehicle_type(), "Taxi")
        self.assertEqual(transport_object.arrival_time(), "7 minutes")
        self.assertEqual(transport_object.travel_time(), "10 minutes")
        self.assertEqual(service.transport_name(), "Taxi")
    def test_bike_service_creation_and_methods(self):
        service = BikeService()
        transport_object = service.create_transport()
        self.assertIsInstance(transport_object, Bike)
        self.assertEqual(transport_object.vehicle_type(), "Bike")
        self.assertEqual(transport_object.arrival_time(), "3 minutes")
        self.assertEqual(transport_object.travel_time(), "20 minutes")
    def test_scooter_service_creation_and_methods(self):
        service = ScooterService()
        transport_object = service.create_transport()
        self.assertIsInstance(transport_object, Scooter)
        self.assertEqual(transport_object.vehicle_type(), "Scooter")
        self.assertEqual(transport_object.arrival_time(), "2 minutes")
        self.assertEqual(transport_object.travel_time(), "15 minutes")
        self.assertEqual(service.transport_name(), "Scooter")
    def test_rollerblades_service_creation_and_methods(self):
        service = RollerbladesService()
        transport_object = service.create_transport()
        self.assertIsInstance(transport_object, Rollerblades)
        self.assertEqual(transport_object.vehicle_type(), "Rollerblades")
        self.assertEqual(transport_object.arrival_time(), "1 minute")
        self.assertEqual(transport_object.travel_time(), "30 minutes")
    def test_bus_service_creation_and_methods(self):
        service = BusService()
        transport_object = service.create_transport()
        self.assertIsInstance(transport_object, Bus)
        self.assertEqual(transport_object.vehicle_type(), "Bus")
        self.assertEqual(transport_object.arrival_time(), "10 minutes")
        self.assertEqual(transport_object.travel_time(), "20 minutes")
    def test_transport_service_default_availability(self):
        service = ScooterService()
        self.assertTrue(service.available)
    def test_transport_service_when_unavailable(self):
        service = ScooterService()
        service.available = False
        self.assertFalse(service.available)

if __name__ == '__main__':
    unittest.main()