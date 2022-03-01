
class Glass(object):
    def __init__(self, i, j, capacity=250, amount=0):
        self.capacity = capacity
        self.amount = amount
        self.overflow = 0
        self.i = i
        self.j = j

    def fill(self, amount_ml):
        overflow = 0

        self.amount += amount_ml
        if (self.amount > self.capacity):
                overflow = self.amount - self.capacity
                self.amount = self.capacity
        self.overflow += overflow

    def get_glass_location_upper_left(self):
        if self.i - 1 < 0:
            return None
        if self.j - 1 < 0:
            return None
        return self.i - 1, self.j - 1

    def get_glass_location_upper_right(self):
        if self.i - 1 < 0:
            return None

        return self.i - 1, self.j

    def get_glass_location_lower_left(self):
        return self.i + 1, self.j

    def get_glass_location_lower_right(self):
        return self.i + 1, self.j + 1

    def __str__(self):
        if not self.get_glass_location_upper_right():
            return str(self.amount) + "\n"
        if not self.get_glass_location_upper_left():
            return str(self.amount) + "-"

        return "-" + str(self.amount) + "-"





glass = Glass(0, 0)
print(glass, glass.overflow, glass.fill(10))
print(glass, glass.overflow, glass.fill(40))
print(glass, glass.overflow, glass.fill(200))
print(glass, glass.overflow, glass.fill(200))

print(glass, glass.overflow)


def instantiate_row(i):
    glasses = []
    for j in range(i + 1):
        glass = Glass(i, j)
        glasses.append(glass)
        return glasses

def fill_glasses(liters, i, j):
    glass_list = [[]]

    amount_ml = liters * 1000

    i = 0

    while amount_ml > 0:
        glasses = instantiate_row(i)

