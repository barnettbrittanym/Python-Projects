from abc import ABC, abstractmethod
class Payments(ABC):
    def paymentDue(self, amount):
        print("Your order total is :", amount)
    @abstractmethod
    def payment(self,amount):
        pass

class CreditCardPayment(Payments):
    def payment(self,amount):
        print ("Your credit card payment amount is :",amount)

class CheckingPayment(Payments):
    def payment(self,amount):
        print ("Your checking account payment amount is:", amount)

obj= CreditCardPayment()
obj.payment(40)
obj.paymentDue(40)

obj= CheckingPayment()
obj.payment(100)
obj.paymentDue(100)
    
