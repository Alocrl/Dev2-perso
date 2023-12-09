import unittest
from unittest.mock import patch
from io import StringIO
from calculator_CLI import Calculator, Blue, Red


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def run_test(self, method, inputs, expected_result, msg):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.calculator.onecmd(f"{method} {inputs}")
            result = mock_stdout.getvalue().strip()
        self.assertEqual(result, Blue(f"Résultat : {expected_result}"), msg)

    def test_add(self):
        # normal
        self.run_test("add", "2 4 7", 13.0, 'test add normal')

        # négatif
        self.run_test("add", "2 -4 7", 5.0, 'test add négatif')

        # négatifs
        self.run_test("add", "2 -4 -7", -9.0, 'test add négatifs')

        # zéro
        self.run_test("add", "2 0 7", 9.0, 'test add zéro')

        # float
        self.run_test("add", "2 4.6 7.2", 13.8, 'test add float')

        # 1 param
        self.run_test("add", "5", 5.0, 'test add 1 param')

        # ValueError
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.calculator.onecmd("add 2 0 a")
            result = mock_stdout.getvalue().strip()
        self.assertEqual(result, Red('Utilisation incorrecte. Exemple : add x y z ...'), 'test add ValueError')

    def test_subtract(self):
        # normal
        self.run_test("subtract", "2 4 7", -9.0, 'test subtract normal')

        # négatif
        self.run_test("subtract", "2 -4 7", -1.0, 'test subtract négatif')

        # négatifs
        self.run_test("subtract", "2 -4 -7", 13.0, 'test subtract négatifs')

        # zéro
        self.run_test("subtract", "2 0 7", -5.0, 'test subtract zéro')

        # float
        self.run_test("subtract", "2 4.6 7.2", -9.8, 'test subtract float')

        # 1 param
        self.run_test("subtract", "5", 5.0, 'test subtract 1 param')

        # ValueError
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.calculator.onecmd("subtract 2 0 a")
            result = mock_stdout.getvalue().strip()
        self.assertEqual(result, Red('Utilisation incorrecte. Exemple : subtract x y z ...'),
                         'test subtract ValueError')

    def test_multiply(self):
        # normal
        self.run_test("multiply", "2 4 7", 56.0, 'test multiply normal')

        # négatif
        self.run_test("multiply", "2 -4 7", -56.0, 'test multiply négatif')

        # négatifs
        self.run_test("multiply", "2 -4 -7", 56.0, 'test multiply négatifs')

        # zéro
        self.run_test("multiply", "2 0 7", 0.0, 'test multiply zéro')

        # float
        self.run_test("multiply", "2 4.6 7.2", 66.24, 'test multiply float')

        # float < 1
        self.run_test("multiply", "4 0.5", 2.0, 'test multiply float < 1')

        # 1 param
        self.run_test("multiply", "5", 5.0, 'test multiply 1 param')

        # ValueError
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.calculator.onecmd("multiply 2 0 a")
            result = mock_stdout.getvalue().strip()
        self.assertEqual(result, Red('Utilisation incorrecte. Exemple : multiply x y z ...'),
                         'test multiply ValueError')

    def test_divide(self):
        # normal
        self.run_test("divide", "70 4 2", 8.75, 'test divide normal')

        # négatif
        self.run_test("divide", "70 -4 2", -8.75, 'test divide négatif')

        # négatifs
        self.run_test("divide", "70 -4 -2", 8.75, 'test divide négatifs')

        # zéro
        self.run_test("divide", "0 2 7", 0.0, 'test divide zéro')

        # float
        self.run_test("divide", "70.2 4.6 2", 7.630, 'test divide float')

        # float < 1
        self.run_test("divide", "4 0.5", 8.0, 'test divide float < 1')

        # 1 param
        self.run_test("divide", "5", 5.0, 'test divide 1 param')

        # ValueError
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.calculator.onecmd("divide 2 4 a")
            result = mock_stdout.getvalue().strip()
        self.assertEqual(result, Red('Utilisation incorrecte. Exemple : divide x y z ...'), 'test divide ValueError')

        # ZeroDivisionError
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.calculator.onecmd("divide 2 0 ")
            result = mock_stdout.getvalue().strip()
        self.assertEqual(result, Red('On ne peut par zéro.'), 'test divide ZeroDivisionError')

    def test_square(self):
        # normal
        self.run_test("square", "2", 4.0, 'test square normal')

        # négatif
        self.run_test("square", "-2", 4.0, 'test square négatif')

        # zéro
        self.run_test("square", "0", 0.0, 'test square zéro')

        # float
        self.run_test("square", "2.5", 6.25, 'test square float')

        # 2 param
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.calculator.onecmd("square 5 4")
            result = mock_stdout.getvalue().strip()
        self.assertEqual(result, Red('Utilisation incorrecte. Exemple : square x'), 'test square ValueError')

        # ValueError
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.calculator.onecmd("square a")
            result = mock_stdout.getvalue().strip()
        self.assertEqual(result, Red('Utilisation incorrecte. Exemple : square x'), 'test square normal')

    def test_power(self):
        # normal
        self.run_test("power", "2 4", 16.0, 'test power normal')

        # négatif
        self.run_test("power", "2 -3", 0.125, 'test power négatif')

        # négatifs
        self.run_test("power", "-2 -3", -0.125, 'test power négatifs')

        # zéro
        self.run_test("power", "2 0", 1.0, 'test power zéro')

        # base zéro
        self.run_test("power", "0 3", 0.0, 'test power base zéro')

        # 0 exp 0
        self.run_test("power", "0 0", 1.0, 'test power 0 exp 0')

        # float
        self.run_test("power", "2 4.6", 24.251, 'test power float')

        # float < 1
        self.run_test("power", "4 0.5", 2.0, 'test power float < 1')

        # 1 param
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.calculator.onecmd("power 5")
            result = mock_stdout.getvalue().strip()
        self.assertEqual(result, Red('Utilisation incorrecte. Exemple : power x y'),
                         'test multiply ValueError')

        # ValueError
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.calculator.onecmd("power 2 a")
            result = mock_stdout.getvalue().strip()
        self.assertEqual(result, Red('Utilisation incorrecte. Exemple : power x y'),
                         'test multiply ValueError')

    def test_sqrt(self):
        # normal
        self.run_test("sqrt", "4", 2.0, 'test sqrt normal')

        # non parfait
        self.run_test("sqrt", "7", 2.646, 'test sqrt non parfait')

        # négatif
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.calculator.onecmd("sqrt -4")
            result = mock_stdout.getvalue().strip()
        self.assertEqual(result, Red('Nombre négatif. La racine carrée n\'est pas définie.'), 'test sqrt négatif')

        # zéro
        self.run_test("sqrt", "0", 0.0, 'test sqrt zéro')

        # float
        self.run_test("sqrt", "2.4", 1.549, 'test sqrt float')

        # 2 param
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.calculator.onecmd("sqrt 5 4")
            result = mock_stdout.getvalue().strip()
        self.assertEqual(result, Red('Utilisation incorrecte. Exemple : sqrt x'), 'test sqrt ValueError')

        # ValueError
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.calculator.onecmd("sqrt a")
            result = mock_stdout.getvalue().strip()
        self.assertEqual(result, Red('Utilisation incorrecte. Exemple : sqrt x'), 'test sqrt normal')

    def test_factorial(self):
        # normal
        self.run_test("factorial", "5", 120, 'test factorial normal')

        # négatif
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.calculator.onecmd("factorial -4")
            result = mock_stdout.getvalue().strip()
        self.assertEqual(result, Red('Nombre négatif. Le factoriel n\'est pas défini.'), 'test factorial négatif')

        # zéro
        self.run_test("factorial", "0", 1, 'test factorial zéro')

        # float
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.calculator.onecmd("factorial 2.4")
            result = mock_stdout.getvalue().strip()
        self.assertEqual(result, Red('Nombre non-entier. Le factoriel n\'est pas défini.'), 'test factorial négatif')

        # 2 param
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.calculator.onecmd("factorial 5 4")
            result = mock_stdout.getvalue().strip()
        self.assertEqual(result, Red('Utilisation incorrecte. Exemple : factorial x'), 'test factorial ValueError')

        # ValueError
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.calculator.onecmd("factorial a")
            result = mock_stdout.getvalue().strip()
        self.assertEqual(result, Red('Utilisation incorrecte. Exemple : factorial x'), 'test factorial normal')

    def test_quit(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertTrue(self.calculator.onecmd("quit"))
            result = mock_stdout.getvalue().strip()
        self.assertEqual(result, Blue("Sortie de la calculatrice !"), 'test quit')
