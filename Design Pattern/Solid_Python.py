from abc import ABC, abstractmethod


class Order:
    items = []
    quantities = []
    prices = []
    status = 'open'

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total


class AUthChecker(ABC):
    @abstractmethod
    def isAuthorized(self):
        pass


class SMSAuthorizer(AUthChecker):
    authorized = False

    def isAuthorized(self) -> bool:
        return self.authorized

    def verify_auth_code(self, code):
        print(f"Verifying code: {code}")
        self.authorized = True


class MachineAuthorizer(AUthChecker):
    isMachine = False

    def isAuthorized(self):
        return self.isMachine

    def not_a_machine(self):
        print("It's not a machine")
        self.isMachine = True


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order):
        pass


class PaymentProcessor_SMS(PaymentProcessor):
    @abstractmethod
    def auth_sms(self, code):
        pass


class DebitPaymentProcessor(PaymentProcessor):

    def __init__(self, security_code, authorizer: AUthChecker):
        self.security_code = security_code
        self.authorizer = authorizer

    def pay(self, order):
        if not self.authorizer.isAuthorized():
            raise Exception("Hacking Attempt.")
        print("Debit payment")
        print(f"Verifying security code: {self.security_code}")
        order.status = 'paid'


class CreditPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code, authorizer: AUthChecker):
        self.security_code = security_code
        self.authorizer = authorizer

    def pay(self, order):
        if not self.authorizer.isAuthorized():
            raise Exception("Hacking Attempt.")
        print("Credit Payment payment")
        print(f"Verifying security code: {self.security_code}")
        order.status = 'paid'


class BkashPaymentProcessor(PaymentProcessor):
    def __init__(self, phone_number, authorizer: AUthChecker):
        self.phone_number = phone_number
        self.authorized = authorizer

    def pay(self, order):
        if not self.authorized.isAuthorized():
            raise Exception("Payment sms code is not verified. ")
        print("Bkash Payment payment")
        print(f"Verifying Phone number: {self.phone_number}")
        order.status = 'paid'


class PaypalPaymentProcessor(PaymentProcessor):
    def __init__(self, email_address, authorizer: AUthChecker):
        self.email_address = email_address
        self.authorized = authorizer

        def pay(self, order):
            if not self.authorized.isAuthorized():
                raise Exception("Payment sms code is not verified. ")

    def pay(self, order):
        if not self.authorized.isAuthorized():
            raise Exception("Payment sms code is not verified. ")
        print("Paypal Payment payment")
        print(f"Verifying Email Address: {self.email_address}")
        order.status = 'paid'


if __name__ == '__main__':
    order = Order()
    order.add_item("Keyboard", 1, 2000)
    order.add_item("Mouse", 3, 750)
    order.add_item("USB cable", 5, 100)
    print(order.total_price())

    sms_auth = SMSAuthorizer()
    robot_checker = MachineAuthorizer()

    robot_checker.not_a_machine()
    payment_debit = DebitPaymentProcessor(12345, robot_checker)
    payment_debit.pay(order)
    print("=====================")

    sms_auth.verify_auth_code(1234)
    payment = PaypalPaymentProcessor("fahadfahim13@gmail.com", sms_auth)
    payment.pay(order)
    print("=====================")

    sms_auth.verify_auth_code(4556)
    payment2 = BkashPaymentProcessor('01732297813', sms_auth)
    payment2.pay(order)
    print("=====================")
