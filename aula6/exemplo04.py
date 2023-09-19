import unittest
from aula6 import somar



class TestSomar(unittest.TestCase):
    def somar_dois_por_dois(self):
        self.assertEqual(somar(2, 2), 3)

    
if __name__ == '__main__':
    unittest.main()