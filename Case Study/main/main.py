from datetime import date
from dao.ICarLeaseImpl import ICarLeaseRepositoryImpl
from entity.customer import Customer
from entity.vehicle import Vehicle

def menu():

    print("1. Add Car")
    print("2. Remove Car")
    print("3. List Available Cars")
    print("4. List Rented Cars")
    print("5. Add Customer")
    print("6. Remove Customer")
    print("7. List Customers")
    print("8. Create Lease")
    print("9. List Active Leases")
    print("10. Lease History")
    print("11. Record Payment for a Lease")
    print("12. Return Car")
    print("13. Total Revenue")
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
        choice = input("Enter your choice (0-13): ")

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
            #print("Car added successfully!!")

        elif choice == "2":
            car_id = int(input("Enter the car ID:"))
            car_repository.removeCar(car_id)

        elif choice == "3":
            available_cars = car_repository.listAvailableCars()
            print("Available Cars:")
            for car in available_cars:
                print(car)

        elif choice == "4":
            rented_cars = car_repository.listRentedCars()
            print("Rented Cars:")
            for car in rented_cars:
                print(car)

        elif choice == "5":
            new_customer = Customer(customerID=int(input("Enter Customer ID: ")),
                                    firstName=input("Enter First Name: "),
                                    lastName=input("Enter Last Name: "),
                                    email=input("Enter Email: "),
                                    phoneNumber=input("Enter Phone Number: "))

            car_repository.addCustomer(new_customer)
            #print("Customer added successfully!!!")

        elif choice == "6":
            cus_id = int(input("Enter the customer id: "))
            car_repository.removeCustomer(cus_id)

        elif choice == "7":
            customers = car_repository.listCustomers()
            print("Customers:")
            for customer in customers:
                print(customer)

        elif choice == "8":
            #start_date = date(2024, 2, 5)
            #end_date = date(2024, 2, 15)
            new_lease = car_repository.createLease(customerID=int(input("Enter Customer ID: ")),
                                                   carID=int(input("Enter Car ID: ")),
                                                   startDate=input("Enter Start Date date(yy-mm-dd): "),
                                                   endDate=input("Enter End Date date(yy-mm-dd): "),
                                                   type = input("Enter the type(monthly or daily): "))
            print("Lease created:", new_lease)

        elif choice == "9":
           ''' active_leases = car_repository.listActiveLeases()
            print("Active Leases:")
            for lease in active_leases:
                print(lease)
'''
           search_date = input("Enter today's date to search for Active Leases :")
           car_repository.listActiveLeases(search_date)

        elif choice == "10":
            date = input("Enter today's date to search for Lease History:")
            car_repository.listLeaseHistory(date)

        elif choice == "11":
            lease_id = int(input("Enter Lease ID: "))
            payment_amount = float(input("Enter Payment Amount: "))
            car_repository.recordPayment(leaseID=lease_id, amount=payment_amount)
            print("Payment recorded successfully!!")

        elif choice == "12":
            lease_id = int(input("Enter Lease ID: "))
            returned_lease = car_repository.returnCar(leaseID=lease_id)
            print("Car returned. Updated Lease information:", returned_lease)

        elif choice == "13":
            car_repository.total_revenue()


        elif choice == "0":
            print("Signing offf Car Rental System. Thanks for Visiting..")
            car_repository.close_connection()
            break

        else:
            print("Invalid choice. Please enter a number between 0 and 13 ")

if __name__ == "__main__":
    main()
