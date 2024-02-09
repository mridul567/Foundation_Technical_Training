import re

class Customer:
    def __init__(self, customerID, firstName, lastName, email, phoneNumber):
        self.customerID = customerID
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.phoneNumber = phoneNumber

        # Getter Methods
    def getCustomerID(self):
            return self.customerID

    def getFirstName(self):
            return self.firstName

    def getLastName(self):
            return self.lastName

    def getEmail(self):
            return self.email

    def getPhoneNumber(self):
            return self.phoneNumber

    # Setter Methods
    def setCustomerID(self, customerID):
            if isinstance(customerID, int) and customerID > 0:
                self.customerID = customerID
            else:
                print("Invalid customerID. It should be a positive integer.")

    def setFirstName(self, firstName):
                if firstName:
                    self.firstName = firstName
                else:
                    print("Invalid first_name. It should not be empty.")

    def setLastName(self, lastName):
                if lastName:
                    self.lastName = lastName
                else:
                    print("Invalid last_name. It should not be empty.")

    def setEmail(self, email):
            self.email = email

    def setPhoneNumber(self, phoneNumber):
            if phoneNumber and re.match(r"\d{10}", phoneNumber):
                self.phoneNumber = phoneNumber
            else:
                print("Invalid phone number format.")
