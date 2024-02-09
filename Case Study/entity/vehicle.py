class Vehicle:
    def __init__(self, vehicleID: int, make : str,
                 model: str,
                 year: int,
                 dailyRate: float,
                 status: str,
                 passengerCapacity: int,
                 engineCapacity: int):
        self.vehicleID = vehicleID
        self.make = make
        self.model = model
        self.year = year
        self.dailyRate = dailyRate
        self.status = status
        self.passengerCapacity = passengerCapacity
        self.engineCapacity = engineCapacity

        # Getter Methods
    def getVehicleID(self):
            return self.vehicleID

    def getMake(self):
            return self.make

    def getModel(self):
            return self.model

    def getYear(self):
            return self.year

    def getDailyRate(self):
            return self.dailyRate

    def getStatus(self):
            return self.status

    def getPassengerCapacity(self):
            return self.passengerCapacity

    def getEngineCapacity(self):
            return self.engineCapacity

    # Setter Methods
    def setVehicleID(self, vehicleID):
            self.vehicleID = vehicleID

    def setMake(self, make):
            self.make = make

    def setModel(self, model):
            self.model = model

    def setYear(self, year):
            set.year = year

    def setDailyRate(self, dailyRate):
            self.dailyRate = dailyRate

    def setStaus(self, status):
        if status not in ['Available', 'NotAvailable']:
            raise Exception("Status should be Available or NotAvailable")
        self.status = status

    def setpassengerCapacity(self, passengerCapacity):
            self.passengerCapacity = passengerCapacity

    def setEngineCapacity(self, engineCapacity):
            self.engineCapacity = engineCapacity

v1 = Vehicle(11,'Honda','City',2015,40.00,'available',
             5,1200)
