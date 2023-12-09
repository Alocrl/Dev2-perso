from unittest import TestCase
from TP07 import Fraction


class TestFraction(TestCase):
    def test_init(self):
        frac = Fraction()
        frac1 = Fraction(8, 2)
        frac2 = Fraction(-8, 2)
        frac3 = Fraction(8, -2)
        frac4 = Fraction(-8, -2)
        frac5 = Fraction(0, 2)

        # défaut
        self.assertEqual(frac.numerator, 0, "test param def")
        self.assertEqual(frac.denominator, 1, "test param def")

        # basique
        self.assertEqual(frac1.numerator, 4, "test num normal")
        self.assertEqual(frac1.denominator, 1, "test den normal")

        # négatif num
        self.assertEqual(frac2.numerator, -4, "test num négatif avec den normal")
        self.assertEqual(frac2.denominator, 1, "test den normal avec num négatif")

        # négatif den
        self.assertEqual(frac3.numerator, -4, "test num normal avec den négatif")
        self.assertEqual(frac3.denominator, 1, "test den négatif avec num normal")

        # négatif num et den
        self.assertEqual(frac4.numerator, 4, "test num négatif avec den négatif")
        self.assertEqual(frac4.denominator, 1, "test den négatif et num négatif")

        # zéro num
        self.assertEqual(frac5.numerator, 0, "test num = 0")
        self.assertEqual(frac5.denominator, 1, "test den avec num = 0")

        # raise: ZeroDivisionError
        self.assertRaises(ZeroDivisionError, Fraction, 1, 0)

    def test_str(self):
        frac = Fraction()
        frac1 = Fraction(8, 2)
        frac2 = Fraction(-8, 2)
        frac3 = Fraction(8, -2)
        frac4 = Fraction(-8, -2)
        frac5 = Fraction(0, 2)

        # 1 défaut
        self.assertEqual(frac.__str__(), "0/1", "test du num déf")

        # 2 normal
        self.assertEqual(frac1.__str__(), "4/1", "test du num normal")

        # 3 négatif num
        self.assertEqual(frac2.__str__(), "-4/1", "test du num négatif")

        # 4 négatif den
        self.assertEqual(frac3.__str__(), "-4/1", "test den négatif")

        # 5 négatif num et den
        self.assertEqual(frac4.__str__(), "4/1", "test num et den négatif")

        # 6 zéro num
        self.assertEqual(frac5.__str__(), "0/1", "test num = 0")

    def test_as_mixed_number(self):
        frac = Fraction()
        frac1 = Fraction(8, 2)
        frac2 = Fraction(-8, 2)
        frac2_2 = Fraction(7, 2)
        frac3 = Fraction(8, -2)
        frac4 = Fraction(-8, -2)
        frac5 = Fraction(0, 2)

        # 1 défaut
        self.assertEqual(frac.as_mixed_number(), "0 + 0/1", "test param def")

        # 2.1 normal
        self.assertEqual(frac1.as_mixed_number(), "4 + 0/2", "test normal")

        # 2.2 normal + reste
        self.assertEqual(frac2_2.as_mixed_number(), "3 + 1/2", "test normal avec reste")

        # 3 négatif num
        self.assertEqual(frac2.as_mixed_number(), "-4 + 0/2", "test num négatif")

        # 4 négatif den
        self.assertEqual(frac3.as_mixed_number(), "-4 + 0/2", "test den négatif")

        # 5 négatif num et den
        self.assertEqual(frac4.as_mixed_number(), "4 + 0/2", "test num et den  négatif")

        # 6 zéro num
        self.assertEqual(frac5.as_mixed_number(), "0 + 0/2", "test num = 0")

    def test_add(self):
        frac = Fraction()
        frac1 = Fraction(8, 2)
        frac2 = Fraction(-8, 2)
        frac3 = Fraction(8, -2)
        frac4 = Fraction(0, 2)

        other = Fraction()
        other1 = Fraction(7, 3)
        other2 = Fraction(-7, 3)
        other3 = Fraction(7, -3)
        other4 = Fraction(-7, -3)
        other5 = Fraction(0, 3)

        # 1 défaut
        self.assertEqual(frac.__add__(other).__str__(), "0/1", "test param def")

        # 2 normal
        self.assertEqual(frac1.__add__(other1).__str__(), "19/3", "test normal")

        # 3 négatif num
        self.assertEqual(frac1.__add__(other2).__str__(), "5/3", "test num négatif ")

        # 4 négatif den
        self.assertEqual(frac3.__add__(other3).__str__(), "-19/3", "test den négatif")

        # 5 négatif num et den
        self.assertEqual(frac1.__add__(other4).__str__(), "19/3", "test num et den négatif")

        # 6 négatif num num et den
        self.assertEqual(frac2.__add__(other4).__str__(), "-5/3", "test 2 num and 1 den négatif")

        # 7 négatif num et den
        self.assertEqual(frac4.__add__(other1).__str__(), "7/3", "test num = 0")

        # 8 zéro num
        self.assertEqual(frac4.__add__(other2).__str__(), "-7/3", "test num = 0 et négatif")

        # 9 zéro num
        self.assertEqual(frac3.__add__(other5).__str__(), "-4/1", "test num = 0 et den négatif ")

    def test_truediv(self):
        frac = Fraction()
        frac1 = Fraction(8, 2)
        frac2 = Fraction(-8, 2)
        frac3 = Fraction(8, -2)
        frac4 = Fraction(-8, -2)
        frac5 = Fraction(0, 2)

        other = Fraction()
        other1 = Fraction(7, 3)
        other2 = Fraction(-7, 3)
        other3 = Fraction(7, -3)
        other5 = Fraction(0, 3)

        # 1 défaut
        self.assertRaises(ZeroDivisionError, frac.__truediv__, other)

        # 2 normal
        self.assertEqual(frac1.__truediv__(other1).__str__(), "12/7", "test param def")

        # 3 négatif num
        self.assertEqual(frac2.__truediv__(other1).__str__(), "-12/7", "test num négatif ")

        # 4 négatif den
        self.assertEqual(frac1.__truediv__(other3).__str__(), "-12/7", "test den négatif")

        # 5 négatif num et den
        self.assertEqual(frac4.__truediv__(other1).__str__(), "12/7", "test num et den négatif")

        # 6 négatif num num et den
        self.assertEqual(frac4.__truediv__(other2).__str__(), "-12/7", "test 2 num et 1 den négatif")

        # 8 zéro num
        self.assertEqual(frac5.__truediv__(other1).__str__(), "0/1", "test num = 0")

        # 9 zéro num
        self.assertEqual(frac5.__truediv__(other2).__str__(), "0/1", "test num = 0 et den négatif")

        # 10 raise : ZeroDivisionError
        self.assertRaises(ZeroDivisionError, frac3.__truediv__, other5)

    def test_eq(self):
        frac = Fraction()
        frac1 = Fraction(8, 2)
        frac2 = Fraction(-8, 2)
        frac3 = Fraction(8, -2)
        frac4 = Fraction(-8, -2)
        frac5 = Fraction(0, 2)

        other = Fraction()
        other1 = Fraction(7, 3)
        other2 = Fraction(8, 2)
        other3 = Fraction(-8, 2)
        other4 = Fraction(0, 3)
        other5 = Fraction(16, 4)

        # 1 défaut
        self.assertEqual(frac.__eq__(other), True, "test param def")

        # 2 normal
        self.assertEqual(frac1.__eq__(other1), False, "test normal")

        # 3 négatif num
        self.assertEqual(frac2.__eq__(other2), False, "test num négatif ")

        # 4 négatif den
        self.assertEqual(frac3.__eq__(other2), False, "test den négatif")

        # 5 négatif num et den
        self.assertEqual(frac4.__eq__(other2), True, "test num et den négatif")

        # 6 négatif num et den
        self.assertEqual(frac3.__eq__(other3), True, "test num et den négatif")

        # 8 zéro num
        self.assertEqual(frac5.__eq__(other4), True, "test num = 0 et den différent")

        # 9 double
        self.assertEqual(frac1.__eq__(other5), True, "test num et den *2 ")

    def test_is_integer(self):
        frac = Fraction()
        frac1 = Fraction(7, 3)
        frac2 = Fraction(8, 2)
        frac3 = Fraction(0, 2)
        frac4 = Fraction(0, -2)
        frac5 = Fraction(3, 4)
        frac6 = Fraction(4, 4)

        # 1 défaut
        self.assertEqual(frac.is_integer(), True, "test param def")

        # 2 normal
        self.assertEqual(frac1.is_integer(), False, "test normal")

        # 3 integer
        self.assertEqual(frac2.is_integer(), True, "test integer")

        # 4 zero
        self.assertEqual(frac3.is_integer(), True, "test num = 0")

        # 5 negative zero
        self.assertEqual(frac4.is_integer(), True, "test num = 0 et den négatif")

        # 6 proper
        self.assertEqual(frac5.is_integer(), False, "test proper")

        # 7 unit
        self.assertEqual(frac6.is_integer(), True, "test unit")

    def test_is_proper(self):
        frac = Fraction()
        frac1 = Fraction(7, 3)
        frac2 = Fraction(8, 2)
        frac3 = Fraction(0, 2)
        frac4 = Fraction(0, -2)
        frac5 = Fraction(3, 4)
        frac6 = Fraction(4, 4)

        # 1 default
        self.assertEqual(frac.is_proper(), True, "test param def")

        # 2 normal
        self.assertEqual(frac2.is_proper(), False, "test normal")

        # 3 integer
        self.assertEqual(frac1.is_proper(), False, "test integer")

        # 4 zero
        self.assertEqual(frac3.is_proper(), True, "test num = 0")

        # 5 negative zero
        self.assertEqual(frac4.is_proper(), True, "test num = 0 et den négatif")

        # 6 proper
        self.assertEqual(frac5.is_proper(), True, "test proper")

        # 7 unit
        self.assertEqual(frac6.is_proper(), False, "test unit")

    def test_is_adjacent_to(self):
        frac = Fraction()
        frac1 = Fraction(8, 2)
        frac2 = Fraction(-8, 2)
        frac3 = Fraction(-2, 2)
        frac4 = Fraction(-8, -2)
        frac5 = Fraction(9, 3)

        other = Fraction()
        other1 = Fraction(7, 2)
        other2 = Fraction(8, 2)
        other3 = Fraction(10, 2)
        other4 = Fraction(6, 2)
        other5 = Fraction(-6, 2)
        other6 = Fraction(0, 2)

        # 1 default
        self.assertEqual(frac.is_adjacent_to(other), False, "test param def")

        # 2 normal
        self.assertEqual(frac1.is_adjacent_to(other1), False, "test normal")

        # 2_2 normal base différente
        self.assertEqual(frac5.is_adjacent_to(other2), True, "test normal base différente")

        # 3 equal
        self.assertEqual(frac1.is_adjacent_to(other2), False, "test égales")

        # 4 adjacent +1
        self.assertEqual(frac1.is_adjacent_to(other3), True, "test adjacent +1")

        # 5 adjacent -1
        self.assertEqual(frac1.is_adjacent_to(other4), True, "test adjacent -1")

        # 6 adjacent -1 negatif
        self.assertEqual(frac2.is_adjacent_to(other5), True, "test adjacent -1 négatif")

        # 7 adjacent -1 negatif et zero
        self.assertEqual(frac3.is_adjacent_to(other6), True, "test adjacent -1 négatif et zéro")

        # 8 adjacent negatif et positif
        self.assertEqual(frac4.is_adjacent_to(other4), True, "test adjacent  négatif et positif")
