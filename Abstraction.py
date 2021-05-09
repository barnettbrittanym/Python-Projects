from abc import ABC, abstractmethod
class Payments(ABC):
    def paymentDue(self, amount):
        print("Your order total is :", amount)
    @abstractmethod
    def payment(self,amount):
        pass

#Creates a class for credit card payments

class CreditCardPayment(Payments):
    def payment(self,amount):
        print ("Your credit card payment amount is :",amount)

#Creates a class to accept checking account payments
class CheckingPayment(Payments):
    def payment(self,amount):
        print ("Your checking account payment amount is:", amount)

obj= CreditCardPayment()
obj.payment(40)
obj.paymentDue(40)

obj= CheckingPayment()
obj.payment(100)
obj.paymentDue(100)
    
