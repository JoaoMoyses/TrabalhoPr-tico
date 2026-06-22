import unittest
import os
from src.dados import carregar_recorde, salvar_recorde

class TestLogicaJogo(unittest.TestCase):
    
    def test_leitura_escrita_recorde(self):
        """Testa se o sistema consegue salvar e carregar o recorde corretamente."""
        arquivo_teste = "recorde_temporario_teste.txt"
        recorde_teste = 999
        
        # Testa a função salvar_recorde
        salvar_recorde(arquivo_teste, recorde_teste)
        
        # Testa a função carregar_recorde
        recorde_lido = carregar_recorde(arquivo_teste)
        
        # Verifica se o que foi lido é igual ao que foi salvo
        self.assertEqual(recorde_lido, recorde_teste)
        
        # Limpa o arquivo temporário depois do teste
        if os.path.exists(arquivo_teste):
            os.remove(arquivo_teste)

if __name__ == '__main__':
    unittest.main()