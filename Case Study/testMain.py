import unittest
from datetime import datetime
from entity.vehicle import Vehicle
from entity.customer import Customer
from entity.lease import Lease
from dao.ICarLeaseImpl import ICarLeaseRepositoryImpl

class TestCarRentalSystem(unittest.TestCase):
    def setUp(self):
        # Replace with your actual MySQL connection details
        connection_params = {
            "host": "localhost",
            "user": "root",
            "password": "9927559686",
            "database": "CarRentalSystem"
        }
        self.car_repository = ICarLeaseRepositoryImpl(connection_params)

    def test_add_car(self):
       ''' new_car = Vehicle(vehicleID=17, make="Toyota", model="Corolla", year=2023, dailyRate=50.00,
                          status="available", passengerCapacity=5, engineCapacity=1500)
        self.car_repository.addCar(new_car)
        # Add assertions to verify if the car was added successfully
        self.assertEqual(new_car.vehicleID, 17)
        self.assertEqual(new_car.make, 'Toyota')
        self.assertEqual(new_car.model, 'Corolla')
        self.assertEqual(new_car.year, 2019)
        self.assertEqual(new_car.dailyRate, 50)
        self.assertEqual(new_car.status, 'available')
        self.assertEqual(new_car.passengerCapacity, 5)
        self.assertEqual(new_car.engineCapacity, 2)
'''
       new_car = Vehicle(vehicleID=23, make="Audi", model="6", year=2023, dailyRate=65.00,
                          status="available", passengerCapacity=4, engineCapacity=1500)
       self.car_repository.addCar(new_car)
       # Add assertions to verify if the car was added successfully
       self.assertEqual(new_car.vehicleID, 23)
       self.assertEqual(new_car.make, 'Audi')
       self.assertEqual(new_car.model, '6')
       self.assertEqual(new_car.year, 2023)
       self.assertEqual(new_car.dailyRate, 65)
       self.assertEqual(new_car.status, 'available')
       self.assertEqual(new_car.passengerCapacity, 4)
       self.assertEqual(new_car.engineCapacity, 1500)

    def test_lease_creation(self):
        new_lease = Lease(leaseID = 17, vehicleID = 8,customerID =8,
                          startDate = "2024-02-18", endDate = "2024-02-20", type = "daily")
        
        self.assertEqual(new_lease.leaseID, 17)
        self.assertEqual(new_lease.vehicleID, 8)
        self.assertEqual(new_lease.customerID, 8)
        self.assertEqual(new_lease.startDate, '2024-02-18')
        self.assertEqual(new_lease.endDate, '2024-02-20')
        self.assertEqual(new_lease.type, 'daily')

if __name__ == "__main__":
    unittest.main()
