"""
class Pessoa
    __init__
        nome str
        sobrenome str
        dados_obtidos bool

    API:
        obter_todos_os_dados -> method
        OK
        404

            (dados obtidos se tornam True se dados obtidos forem OK)
"""
import unittest
from unittest.mock import patch
from pessoa import Pessoa

class TestPessoa(unittest.TestCase):
    def setUp(self):
        self.pessoa = Pessoa("João", "Silva")
        self.pessoa2 = Pessoa("Maria", "Souza")

    def test_pessoa_attr_nome_tem_o_valor_correto(self):
        self.assertEqual(self.pessoa.nome, "João")
        self.assertEqual(self.pessoa2.nome, "Maria")

    def test_pessoa_attr_nome_e_str(self):
        self.assertIsInstance(self.pessoa.nome, str)
        self.assertIsInstance(self.pessoa2.nome, str)

    def test_pessoa_attr_sobrenome_tem_o_valor_correto(self):
        self.assertEqual(self.pessoa.sobrenome, "Silva")
        self.assertEqual(self.pessoa2.sobrenome, "Souza")
    
    def test_pessoa_attr_sobrenome_e_str(self):
        self.assertIsInstance(self.pessoa.sobrenome, str)
        self.assertIsInstance(self.pessoa2.sobrenome, str)
    
    def test_pessoa_attr_dados_obtidos_tem_o_valor_correto(self):
        self.assertFalse(self.pessoa.dados_obtidos)
        self.assertFalse(self.pessoa2.dados_obtidos)
    
    def test_obter_todos_os_dados_sucesso_OK(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = True

            self.assertEqual(self.pessoa.obter_todos_os_dados(), 'CONECTADO')
            self.assertTrue(self.pessoa.dados_obtidos)

            self.assertEqual(self.pessoa2.obter_todos_os_dados(), 'CONECTADO')
            self.assertTrue(self.pessoa2.dados_obtidos)
    
    def test_obter_todos_os_dados_falha_404(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = False
            fake_request.return_value.status_code = 404

            self.assertEqual(self.pessoa.obter_todos_os_dados(), 'ERRO 404')
            self.assertFalse(self.pessoa.dados_obtidos)

            self.assertEqual(self.pessoa2.obter_todos_os_dados(), 'ERRO 404')
            self.assertFalse(self.pessoa2.dados_obtidos)

    def test_obter_todos_os_dados_secesso_e_falha(self):
        with patch('requests.get') as fake_request:
            # Simula sucesso
            fake_request.return_value.ok = True
            self.assertEqual(self.pessoa.obter_todos_os_dados(), 'CONECTADO')
            self.assertTrue(self.pessoa.dados_obtidos)

            self.assertEqual(self.pessoa2.obter_todos_os_dados(), 'CONECTADO')
            self.assertTrue(self.pessoa2.dados_obtidos)

            # Simula falha
            fake_request.return_value.ok = False
            fake_request.return_value.status_code = 404
            
            self.assertEqual(self.pessoa.obter_todos_os_dados(), 'ERRO 404')
            self.assertFalse(self.pessoa.dados_obtidos)

            self.assertEqual(self.pessoa2.obter_todos_os_dados(), 'ERRO 404')
            self.assertFalse(self.pessoa2.dados_obtidos)



if __name__ == '__main__':
    unittest.main(verbosity=2)