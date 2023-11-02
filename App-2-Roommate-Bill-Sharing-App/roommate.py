class Bill:
    """
    Object that contains data about a bill, such as total amount and period of the bill
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period

class Roommate:
    """
    Creates a roommate person who lives in the apartment and pays a share to the bill
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, other_roommate):
        weight = self.days_in_house / (self.days_in_house + other_roommate.days_in_house)
        to_pay = bill.amount * weight
        return to_pay