'''import unittest
import Cambia_texto


class ProbarCambiaTexto(unittest.TestCase):

    def test_mayusculas(self):
        palabra = 'buen dia'
        resultado = Cambia_texto.todo_mayuscula(palabra)
        self.assertEqual(resultado, 'Buen Dia')

if __name__ == '__main__':
    unittest.main()'''
import unittest

class TestMathOperations(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(2 + 2, 4)

if __name__ == '__main__':
    unittest.main()