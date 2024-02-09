class Payment:
    def __init__(self, paymentID, leaseID, paymentDate, amount):
        self.paymentID = paymentID
        self.leaseID = leaseID
        self.paymentDate = paymentDate
        self.amount = amount

    #Getter Methods
    def getPaymentID(self):
        return self.paymentID

    def getLeaseID(self):
        return self.leaseID

    def getPaymentDate(self):
        return self.paymentDate

    def getAmount(self):
        return self.amount

    #Setter Methods
    def setPaymentID(self,paymentID):
        self.paymentID = paymentID

    def setLeaseID(self,leaseID):
        self.leaseID = leaseID

    def setPaymentDate(self,paymentDate):
        self.paymentDate = paymentDate

    def setAmount(self,amount):
        self.amount = amount

