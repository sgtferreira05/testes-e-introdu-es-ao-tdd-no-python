try:
    import sys
    import os

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                  '..\src'))
    )
except ImportError:
    print("Erro ao importar módulos necessários para os testes.")
    sys.exit(1)


import unittest
from src.calculadora import soma, subtracao

class TestCalculadora(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(soma(2, 3), 5)

    def test_subtracao(self):
        self.assertEqual(subtracao(5, 2), 3)

    def test_soma_varias_entradas(self):
        # self.assertEqual(soma(10, 20), 30)
        # self.assertEqual(soma(-15, 25), 10)
        # self.assertEqual(soma(3.5, 2.5), 6.0)
        x_y_pairs = [(10, 20), (-15, 25), (3.5, 2.5)]
        expected_results = [30, 10, 6.0]

        for (x, y), expected in zip(x_y_pairs, expected_results):
            with self.subTest(x=x, y=y):
                self.assertEqual(soma(x, y), expected)

    def test_soma_x_nao_numero(self):
        with self.assertRaises(AssertionError) as context:
            soma('10', 20)
        self.assertEqual(str(context.exception), "O primeiro argumento deve ser um número")

    def test_soma_y_nao_numero(self):
        with self.assertRaises(AssertionError) as context:
            soma(10, '20')
        self.assertEqual(str(context.exception), "O segundo argumento deve ser um número")

if __name__ == '__main__':
    unittest.main(verbosity=2)