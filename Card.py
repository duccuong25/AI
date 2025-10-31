class CreditCard:
    """ A consumer credit card. """

    def __init__(self, customer, bank, acnt, limit):
        """Create a new credit card instance.
        The initial balance is zero.
        """
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        """Return name of the customer."""
        return self._customer

    def get_bank(self):
        """Return the bank's name."""
        return self._bank

    def get_account(self):
        """Return the card identifying number (string)."""
        return self._account

    def get_limit(self):
        """Return current credit limit."""
        return self._limit

    def get_balance(self):
        """Return current balance."""
        return self._balance

    def charge(self, price):
        """Charge given price to the card, if limit allows.
        Return True if charge processed; False if denied.
        """
        if price + self._balance > self._limit:  # nếu vượt hạn mức
            return False
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        """Process customer payment that reduces balance."""
        self._balance -= amount


# ----------------- TEST -----------------
if __name__ == "__main__":
    card = CreditCard("John Bowman", "California Savings", "5391 0375 9387 5309", 1000)

    print("Khách hàng:", card.get_customer())
    print("Ngân hàng:", card.get_bank())
    print("Tài khoản:", card.get_account())
    print("Hạn mức:", card.get_limit())
    print("Số dư ban đầu:", card.get_balance())

    # Thử charge
    print("\nMua hàng giá 200:", card.charge(200))
    print("Số dư hiện tại:", card.get_balance())

    print("Mua hàng giá 900:", card.charge(900))  # vượt hạn mức
    print("Số dư hiện tại:", card.get_balance())

    # Thanh toán
    card.make_payment(100)
    print("\nSau khi trả 100, số dư:", card.get_balance())
