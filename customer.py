class Customer:
    def __init__(self, name):
        self.name = name

    def order_transport(self, service):
        print(f"Klient {self.name} składa zamówienie:")
        service.order_transport()