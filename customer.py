"""
Moduł customer.py
-----------------
Zawiera klasę reprezentującą klienta systemu korzystającego z usług transportowych.
"""

class Customer:
    """
    Klasa reprezentująca klienta, który wchodzi w interakcję z systemem
    i może zamawiać wybrane usługi transportowe.
    """
    def __init__(self, name):
        """Inicjalizuje obiekt klienta podanym imieniem."""
        self.name = name

    def order_transport(self, service):
        """Wywołuje proces zamówienia określonej usługi transportowej dla klienta."""
        print(f"Klient {self.name} składa zamówienie:")
        service.order_transport()