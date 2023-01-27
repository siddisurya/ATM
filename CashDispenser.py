class CashDispenser:
    def __init__(self):
        self.notes = {"$20": 0, "$50": 0}

    def add_cash(self, denomination, count):
        if denomination not in self.notes:
            print("Invalid denomination")
            return
        self.notes[denomination] += count

    def get_notes(self):
        return self.notes

    def remove_cash(self, denomination, count):
        if denomination not in self.notes:
            return "Invalid denomination"
        if self.notes[denomination] < count:
            return "Not enough cash available"
        self.notes[denomination] -= count
        return self.notes

    def cash_dispense(self, amount):
        if amount % 10 != 0:
            print("Invalid amount")
            return
        if amount > (self.notes["$20"] * 20 + self.notes["$50"] * 50):
            print("Not enough cash available")
            return
        denominations = {"$20": 0, "$50": 0}
        while amount >= 50 and self.notes["$50"] > 0:
            amount -= 50
            self.notes["$50"] -= 1
            denominations["$50"] += 1
        while amount >= 20 and self.notes["$20"] > 0:
            amount -= 20
            self.notes["$20"] -= 1
            denominations["$20"] += 1
        if amount == 0:
            return denominations
        else:
            self.add_cash("$50", denominations["$50"])
            self.add_cash("$20", denominations["$20"])
            return "Cannot dispense the given amount"

