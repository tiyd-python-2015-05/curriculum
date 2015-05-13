class Money:
    def __init__(self, amount, currency_code):
        self.amount = amount
        self.currency_code = currency_code

    def __eq__(self, other):
        return self.amount == other.amount and \
            self.currency_code == other.currency_code

    def __add__(self, other):
        try:
            if self.currency_code != other.currency_code:
                raise ValueError("You cannot add {} to {}".format(
                    self.currency_code, other.currency_code))
            return Money(self.amount + other.amount, self.currency_code)
        except AttributeError:
            raise TypeError("Cannot add {} to Money".format(type(other)))

    @classmethod
    def usd(cls, amount):
        return cls(amount, "USD")
