# Author: Sunil Shah
# Date: 10/28/24
# Description: This program demonstrates the Factory Pattern and Adapter Pattern.
# Class: Advanced Software Paradigms, Fall 2024

from abc import ABC, abstractmethod

# --- Creational Pattern: Factory Pattern for creating Vehicle objects ---

class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        return "Car is moving"

class Plane(Vehicle):
    def move(self):
        return "Plane is flying"

class VehicleFactory:
    @staticmethod
    def create_vehicle(vehicle_type: str) -> Vehicle:
        if vehicle_type.lower() == 'car':
            return Car()
        elif vehicle_type.lower() == 'plane':
            return Plane()
        else:
            raise ValueError("Unknown vehicle type")

# --- Structural Pattern: Adapter Pattern to unify interaction with the Vehicle ---

class VehicleInterface(ABC):
    @abstractmethod
    def get_movement(self):
        pass


class VehicleAdapter(VehicleInterface):
    def __init__(self, vehicle: Vehicle):
        self.vehicle = vehicle
    
    def get_movement(self):
        return self.vehicle.move()

# --- Function utilizing both patterns ---

def create_and_interact_with_garage(vehicle_type: str) -> str:
    vehicle = VehicleFactory.create_vehicle(vehicle_type)
    vehicle_adapter = VehicleAdapter(vehicle)
    return vehicle_adapter.get_movement()

# --- Main/Test function ---

def main():
    vehicle_movement = create_and_interact_with_garage('car')
    print("Car movement:", vehicle_movement)

    vehicle_movement = create_and_interact_with_garage('plane')
    print("Plane movement:", vehicle_movement)

if __name__ == "__main__":
    main()
