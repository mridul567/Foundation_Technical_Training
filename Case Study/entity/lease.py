class Lease:
    def __init__(self, leaseID, vehicleID, customerID, startDate, endDate,type):
        self.leaseID = leaseID
        self.vehicleID = vehicleID
        self.customerID = customerID
        self.startDate = startDate
        self.endDate = endDate
        self.type = type

    @property
    def getLeaseID(self):
        return self.leaseID

    @property
    def getVehicleID(self):
        return self.vehicleID

    @property
    def getCustomerID(self):
        return self.customerID

    @property
    def getStartDate(self):
        return self.startDate

    @property
    def getEndDate(self):
        return self.endDate

    @property
    def getType(self):
        return self.type

    def setLeaseID(self, value):
        self.leaseID = value

    def setVehicleID(self, value):
        self.vehicleID = value

    def setCustomerID(self, value):
        self.customerID = value

    def setStartDate(self, value):
        self.startDate = value

    def setEndDate(self, value):
        self.endDate = value

    def setType(self, value):
        self.type = value


l1 = Lease(17, 8,  8,  "2024-02-18", "2024-02-20","daily")
