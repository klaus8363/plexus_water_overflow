
class Glass(object):
    def __init__(self, i, j, capacity=250, amount=0):
        self.capacity = capacity
        self.amount = amount
        self.i = i
        self.j = j

    def fill(self, amount_ml):
        overflow = 0
        if amount_ml > self.capacity:
            self.amount = self.capacity
            overflow = amount_ml - self.capacity
        else:
            self.amount = amount_ml

        return overflow
