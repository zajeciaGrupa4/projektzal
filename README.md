# Dokumentacja Projektu Systemu Rezerwacji Transportu

## 1. Opis modułów i klas
Projekt składa się z czterech głównych modułów napisanych w języku Python:

*   **`transport.py`**: Definiuje strukturę produktów. Zawiera klasę abstrakcyjną `Transport` oraz klasy konkretne: `Taxi`, `Bike`, `Scooter`. Odpowiada za cechy specyficzne dla każdego środka lokomocji (czas przyjazdu, czas podróży).
*   **`services.py`**: Zawiera logikę biznesową (proces zamówienia i walidację dostępności). Definiuje klasę bazową `TransportServices` oraz podklasy fabrykujące: `TaxiService`, `BikeService`, `ScooterService`.
*   **`customer.py`**: Odpowiada za klasę `Customer`, która symuluje zachowanie klienta zlecającego zamówienie transportu za pomocą przekazanej usługi.
*   **`main.py`**: Punkt wejścia do aplikacji służący do demonstracji działania całego systemu.

## 2. Opis wzorca projektowego Factory Method (Metoda Fabrykująca)
W projekcie zastosowano kreacyjny wzorzec projektowy **Factory Method**. 
*   **Problem:** Klient potrzebuje zamówić środek transportu, ale system nie powinien być sztywno powiązany z konkretnymi klasami pojazdów, aby ułatwić dodawanie nowych rodzajów transportu w przyszłości.
*   **Rozwiązanie:** Klasa `TransportServices` definiuje abstrakcyjną metodę `create_transport()`. Konkretne klasy usług (np. `TaxiService`) implementują tę metodę, decydując, który dokładnie obiekt transportu utworzyć. Dzięki temu logika zamawiania (`order_transport`) jest uniwersalna i odizolowana od szczegółów technicznych poszczególnych pojazdów.

## 3. Instrukcja uruchomienia projektu
Aby uruchomić aplikację lokalnie na swoim komputerze, wykonaj następujące kroki:

1. Upewnij się, że masz zainstalowane środowisko Python (zalecana wersja 3.8 lub nowsza).
2. Otwórz terminal (wiersz poleceń) i przejdź do katalogu z projektem:
```bash
   cd sciezka/do/twojego/projektu
