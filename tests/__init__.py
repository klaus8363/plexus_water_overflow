import unittest
from main import Glass
from main import GlassFiller


class GlassTest(unittest.TestCase):
    glass = Glass(0, 0)
    glass_1_0 = Glass(1, 0)
    glass_1_1 = Glass(1, 1)

    def test_initial_glass(self):
        self.glass.fill(200)
        self.assertEqual(self.glass.amount, 200)
        self.glass.fill(50)
        self.assertEqual(self.glass.amount, 250)

    def test_upper_left_of_glass(self):
        self.assertEqual(self.glass.get_glass_location_upper_left(), None)

    def test_upper_right_of_glass(self):
        self.assertEqual(self.glass.get_glass_location_upper_right(), None)

    def test_upper_values_child_0(self):
        self.assertEqual(self.glass_1_0.get_glass_location_upper_left(), None)
        self.assertEqual(self.glass_1_0.get_glass_location_upper_right(), (0, 0))


    def test_upper_values_child_1(self):
        self.assertEqual(self.glass_1_1.get_glass_location_upper_left(), (0, 0))
        self.assertEqual(self.glass_1_1.get_glass_location_upper_right(), None)

    def test_remaining_capacity(self):
        self.assertEqual(self.glass_1_0.get_remaining_capacity(), 250)
        self.glass_1_0.fill(100)
        self.assertEqual(self.glass_1_0.get_remaining_capacity(), 150)
        self.glass_1_0.fill(100)
        self.assertEqual(self.glass_1_0.get_remaining_capacity(), 50)
        self.glass_1_0.fill(50)
        self.assertEqual(self.glass_1_0.get_remaining_capacity(), 0)
        self.glass_1_0.fill(50)
        self.assertEqual(self.glass_1_0.get_remaining_capacity(), 0)

    def test_overflow_values(self):
        self.assertEqual(self.glass_1_1.overflow, 0)
        self.glass_1_1.fill(100)
        self.assertEqual(self.glass_1_1.overflow, 0)
        self.glass_1_1.fill(100)
        self.assertEqual(self.glass_1_1.overflow, 0)
        self.glass_1_1.fill(100)
        self.assertEqual(self.glass_1_1.overflow, 50)
        self.glass_1_1.fill(100)
        self.assertEqual(self.glass_1_1.overflow, 150)


class GlassFillerTest(unittest.TestCase):
    glass_filler = GlassFiller(1.5, 2, 2)

    def test_glass_filler(self):
        self.assertEqual(self.glass_filler.fill_glasses(), 187.5)
        self.assertEqual(self.glass_filler.glass_list[0][0].amount, 250)


    def test_all_values(self):
        values = [
            [250], 
            [250, 250],
            [187.5, 250, 187.5],
            [0, 62.5, 62.5, 0],
        ]
        self.glass_filler.fill_glasses()
        test_values = self.glass_filler.glass_list

        a = 0
        for glass_row in test_values:
            b = 0
            for glass in glass_row:
                self.assertEqual(glass.amount, values[a][b])
                b += 1
            a += 1




