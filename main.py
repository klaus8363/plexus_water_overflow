
class Glass(object):
    # Assumption: all amount/capacity in this object is in mL
    def __init__(self, i, j, capacity=250, amount=0):
        self.capacity = capacity
        self.amount = amount
        self.overflow = 0
        self.i = i
        self.j = j

    def will_overflow(self, amount_ml):
        if self.amount + amount_ml > self.capacity:
            return True
        return False

    def get_remaining_capacity(self):
        return self.capacity - self.amount

    def get_overflow(self, amount_to_add):
        if amount_to_add > self.get_remaining_capacity():
            return amount_to_add - self.get_remaining_capacity()
        return False

    def fill(self, amount_ml):
        overflow = 0

        if self.get_overflow(amount_ml):
            overflow = self.get_overflow(amount_ml)
            self.amount = self.capacity
            self.overflow += overflow

        else:
            self.amount += amount_ml

        return self.overflow

    def get_glass_location_upper_left(self):
        if self.i - 1 < 0:
            return None
        if self.j - 1 < 0:
            return None
        return self.i - 1, self.j - 1

    def get_glass_location_upper_right(self):
        if self.i - 1 < 0:
            return None
        if self.i == self.j:
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


# Assumptions:
'''
1) this class only accepts liters as input. It will be converted to ml then processed.
2) this only accepts correct input. Out of bounds i, and j values will return an error 
'''
class GlassFiller(object):

    def __init__(self, input_liters=1.5,
        i_tocheck=0, j_tocheck=0, show_all_values=False):

        self.input_liters = input_liters
        self.i_tocheck = i_tocheck
        self.j_tocheck = j_tocheck
        self.glass_list = []
        self.show_all_values = show_all_values

    def initialize_row(self, row_):
        glasses = []

        for i in range(row_ + 1):
            glass = Glass(row_, i)
            glasses.append(glass)
        return glasses

    def fill_glasses(self):
        i = self.i_tocheck
        j = self.j_tocheck
        amount_ml = self.input_liters * 1000

        current_row = 0
        next_row_needed = True

        while next_row_needed:
            glasses = self.initialize_row(current_row)
            self.glass_list.append(glasses)

            glass_overflows = False
            for glass in glasses:

                if current_row == 0:
                    overflow = glass.fill(amount_ml)
                    if overflow > 0:
                        glass_overflows = True

                else:
                    if glass.get_glass_location_upper_left() is not None:
                        ul_i, ul_j = glass.get_glass_location_upper_left()
                        glass_parent = self.glass_list[ul_i][ul_j]

                        overflow = glass.fill(glass_parent.overflow / 2)

                        if overflow > 0:
                            glass_overflows = True

                    if glass.get_glass_location_upper_right() is not None:
                        ur_i, ur_j = glass.get_glass_location_upper_right()

                        glass_parent = self.glass_list[ur_i][ur_j]
                        overflow = glass.fill(glass_parent.overflow / 2)

                        if overflow > 0:
                            glass_overflows = True

            current_row += 1
            if glass_overflows:
                next_row_needed = True
            else:
                next_row_needed = False

        if self.show_all_values:
            a = 0
            for glass_row in self.glass_list:
                print("i={}".format(a))
                b = 0
                for glass in glass_row:
                    print("j={}: value={}".format(b, glass.amount))
                    b += 1
                a += 1
                print("-----------------")

        return self.glass_list[i][j].amount


def main():
    k = GlassFiller(1.5, 2, 2, True)
    print("Value at i={}, j={} : {}".format(
        k.i_tocheck, k.j_tocheck, k.fill_glasses()))


if __name__ == "__main__":
    main()
