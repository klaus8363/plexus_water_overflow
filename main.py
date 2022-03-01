
class Glass(object):
    def __init__(self, i, j, capacity=250, amount=0):
        self.capacity = capacity
        self.amount = amount
        self.overflow = 0
        self.i = i
        self.j = j

    def will_overflow(self, amount_ml):
        if self.amount + amount_ml > self.capacity:
            # print("WO", self.amount, amount_ml, self.capacity)
            return True
        return False

    def is_full(self):
        return self.amount == self.capacity

    def get_remaining_capacity(self):
        return self.capacity - self.amount

    def get_overflow(self, amount_to_add):
        if amount_to_add > self.get_remaining_capacity():
            # print("Amt to add", amount_to_add, "capacity", self.get_remaining_capacity())
            return amount_to_add - self.get_remaining_capacity()
        return False

    def fill(self, amount_ml):
        overflow = 0
        amt_to_add = 0

        if self.get_overflow(amount_ml):
            # print("entered")
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
'''
glass = Glass(0, 0)


print(glass, glass.overflow, glass.fill(1000))
glass.fill(1000)

print(glass, glass.overflow)
'''

def initialize_row(row_):
    print("ROW INPUT", row_)
    glasses = []

    for i in range(row_ + 1):
        print("I, range, ", i, row_)
        glass = Glass(row_, i)
        glasses.append(glass)
    return glasses


def fill_glasses(liters, i, j):
    glass_list = []

    amount_ml = liters * 1000

    current_row = 0
    next_row_needed = True

    while next_row_needed:
        glasses = initialize_row(current_row)
        glass_list.append(glasses)

        glass_overflows = False
        print("created glasses:", len(glasses))
        for glass in glasses:

            if current_row == 0:
                overflow = glass.fill(amount_ml)
                if overflow > 0:
                    glass_overflows = True

            else:
                print("I is now:", current_row)
                print("glass location: ", glass.i, glass.j)
                
                if glass.get_glass_location_upper_left() is not None:
                    ul_i, ul_j = glass.get_glass_location_upper_left()
                    glass_parent = glass_list[ul_i][ul_j]
                    print("UPPERLEFT", ul_i, ul_j)
                    print("Glass parent:", glass_parent.overflow)

                    overflow = glass.fill(glass_parent.overflow / 2)

                    if overflow > 0:
                        glass_overflows = True

                if glass.get_glass_location_upper_right() is not None:
                    ur_i, ur_j = glass.get_glass_location_upper_right()

                    glass_parent = glass_list[ur_i][ur_j]
                    print("UPPERIGHT", ur_i, ur_j)
                    print("Glass parent:", glass_parent.overflow)

                    overflow = glass.fill(glass_parent.overflow / 2)

                    if overflow > 0:
                        glass_overflows = True



        current_row += 1
        if glass_overflows:
            next_row_needed = True
        else:
            next_row_needed = False


    for gl in glass_list:
        for a in gl:
            print("S", a)




'''
    while next_row_needed:
        glasses = instantiate_row(i)
        glass_list.append(glasses)

        glass_overflows = False
        print("I is", i, *glasses)
        for glass in glasses:

            if i == 0:
                will_overflow = glass.fill(amount_ml)
            else:

                if glass.get_glass_location_upper_left():
                    ul_i, ul_j = glass.get_glass_location_upper_left()

                    print("Upperleft:", ul_i, ul_j, glass_list[ul_i, ul_j])

                    break

            

            if will_overflow:
                ## need new rows
                amount_ml -= glass.capacity
                print("A", glass)
                glass_overflows = True

        i += 1

        if glass_overflows:
            next_row_needed = True
        else:
            next_row_needed = False

'''

fill_glasses(1.5, 0, 0)

