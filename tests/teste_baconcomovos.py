"""
TDD: Test Driven Development (Desenvolvimento Orientado a Testes)

Part 1 (RED): Create a test that fails
Part 2 (GREEN): Create the minimum code to make the test pass
Part 3 (BLUE): Refactor the code to make it better
"""

try:
    import sys
    import os

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                    '..\src'))  #type: ignore
    )
except ImportError:
    print("Erro ao importar módulos necessários para os testes.")
    sys.exit(1)

import unittest
from src.baconcomovos import bacon_com_ovos

class TestBaconComOvos(unittest.TestCase):
    def test_bacon_com_ovos_deve_levantar_assertion_error_se_valor_nao_for_inteiro(self):
        with self.assertRaises(AssertionError):
            bacon_com_ovos("string")
    
    def test_bacon_com_ovos_deve_retornar_bacon_com_ovos_se_valor_for_multiplo_de_3_e_5(self):
        entradas = [15, 30, 45, 60]
        saida = "Bacon com ovos"
        
        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(
                    bacon_com_ovos(entrada),
                    saida, 
                    msg=f"Entrada: {entrada}, Saída esperada: {saida}")


    def test_bacon_com_ovos_deve_retornar_bacon_se_valor_for_multiplo_de_3(self):
        entradas = [3, 6, 9, 12]
        saida = "Bacon"
        
        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_com_ovos(entrada), saida)
    def test_bacon_com_ovos_deve_retornar_ovos_se_valor_for_multiplo_de_5(self):
        entradas = [5, 10, 20, 25]
        saida = "Ovos"
        
        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_com_ovos(entrada), saida)
    def test_bacon_com_ovos_deve_retornar_sem_cafe_se_valor_nao_for_multiplo_de_3_ou_5(self):
        entradas = [1, 2, 4, 7, 8]
        saida = "Sem café"
        
        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_com_ovos(entrada), saida)

if __name__ == '__main__':
    unittest.main(verbosity=2)
