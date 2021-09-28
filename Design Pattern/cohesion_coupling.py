import string
import random


class VehicleInfo:
    brand: str
    catalogue_price: int
    electric: bool

    def __init__(self, brand, catalogue_price, electric):
        self.brand = brand
        self.catalogue_price = catalogue_price
        self.electric = electric

    def get_tax(self):
        if self.electric:
            return 0.02
        return 0.05

    def compute_tax(self):
        return self.get_tax() * self.catalogue_price

    def print_tax(self):
        print(f"Brand: {self.brand}")
        print(f"Payable Tax: {self.compute_tax()}")


class Vehicle:
    id: str
    license_plate: str
    info: VehicleInfo

    def __init__(self, id, license_plate, info):
        self.id = id
        self.info = info
        self.license_plate = license_plate

    def print_vehicle(self):
        print(f"Id: {self.id}")
        print(f"License Plate: {self.license_plate}")
        self.info.print_tax()


class VehicleRegistration:
    vehicle_info = {}

    def __init__(self):
        self.add_vehicle_info("Tesla Model 3", 60000, True)
        self.add_vehicle_info("Volkswagen ID3", 35000, True)
        self.add_vehicle_info("BMW 5", 45000, False)

    def add_vehicle_info(self, brand, catalogue_price, electric):
        self.vehicle_info[brand] = VehicleInfo(brand, catalogue_price, electric)

    def generate_vehicle_id(self, length):
        return "".join(random.choices(string.ascii_uppercase, k=length))

    def generate_vehicle_licence(self, id):
        return f"{id[:2]}-{''.join(random.choices(string.digits, k=2))}-{''.join(random.choices(string.ascii_uppercase, k=2))}"

    def create_vehicle(self, brand: str):
        vehicle_id = self.generate_vehicle_id(12)
        license_plate = self.generate_vehicle_licence(vehicle_id)
        return Vehicle(vehicle_id, license_plate, self.vehicle_info[brand])


class Applications:

    def register_vehicle(self, brand: str):
        registry = VehicleRegistration()
        return registry.create_vehicle(brand)


if __name__ == '__main__':
    app = Applications()
    vehicle = app.register_vehicle("Volkswagen ID3")
    vehicle.print_vehicle()
