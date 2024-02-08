from datetime import date
from dao.ICarLeaseImpl import ICarLeaseRepositoryImpl
from entity.customer import Customer
from entity.vehicle import Vehicle

def menu():

    print("1. Add  Car")
    print("2. List Available Cars")
    print("3. Add  Customer")
    print("4. List Customers")
    print("5. Create  Lease")
    print("6. List Active Leases")
    print("7. Record Payment for a Lease")
    print("8. Return  Car")
    print("0. Exit")

def main():
    # Replace with your actual MySQL connection details
    connection_params = {
        "host": "localhost",
        "user": "root",
        "password": "9927559686",
        "database": "CarRentalSystem"
    }

    car_repository = ICarLeaseRepositoryImpl(connection_params)

    while True:
        print("\n--- Welcome to Car Rental System------")
        menu()
        choice = input("Enter your choice (0-8): ")

        if choice == "1":
            new_car = Vehicle(vehicleID=int(input("Enter Vehicle ID: ")),
                              make=input("Enter Make: "),
                              model=input("Enter Model: "),
                              year=int(input("Enter Year: ")),
                              dailyRate=float(input("Enter Daily Rate: ")),
                              status=input("Enter Status (available/notAvailable): "),
                              passengerCapacity=int(input("Enter Passenger Capacity: ")),
                              engineCapacity=int(input("Enter Engine Capacity: ")))

            car_repository.addCar(new_car)
            print("Car added successfully!!")

        elif choice == "2":
            available_cars = car_repository.listAvailableCars()
            print("Available Cars:")
            for car in available_cars:
                print(car)

        elif choice == "3":
            new_customer = Customer(customerID=int(input("Enter Customer ID: ")),
                                    firstName=input("Enter First Name: "),
                                    lastName=input("Enter Last Name: "),
                                    email=input("Enter Email: "),
                                    phoneNumber=input("Enter Phone Number: "))

            car_repository.addCustomer(new_customer)
            print("Customer added successfully!!!")

        elif choice == "4":
            customers = car_repository.listCustomers()
            print("Customers:")
            for customer in customers:
                print(customer)

        elif choice == "5":
            start_date = date(2024, 2, 5)
            end_date = date(2024, 2, 20)
            new_lease = car_repository.createLease(customerID=int(input("Enter Customer ID: ")),
                                                   carID=int(input("Enter Car ID: ")),
                                                   startDate=start_date,
                                                   endDate=end_date)
            print("Lease created:", new_lease)

        elif choice == "6":
            active_leases = car_repository.listActiveLeases()
            print("Active Leases:")
            for lease in active_leases:
                print(lease)

        elif choice == "7":
            lease_id = int(input("Enter Lease ID: "))
            payment_amount = float(input("Enter Payment Amount: "))
            car_repository.recordPayment(leaseID=lease_id, amount=payment_amount)
            print("Payment recorded successfully!!")

        elif choice == "8":
            lease_id = int(input("Enter Lease ID: "))
            returned_lease = car_repository.returnCar(leaseID=lease_id)
            print("Car returned. Updated Lease information:", returned_lease)

        elif choice == "0":
            print("Signing offf Car Rental System. Thanks for Visiting..")
            car_repository.close_connection()
            break

        else:
            print("Invalid choice. Please enter a number between 0 and 8.")

if __name__ == "__main__":
    main()