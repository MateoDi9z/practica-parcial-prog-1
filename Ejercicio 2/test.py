import io
import unittest.mock
from main import main

ej1 = "Bruno Almiron Alma Giuliano Juan Cruz Gonzalez"

class Test(unittest.TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_ex(self, mock_stdout):
      #* Test OK - 1
      result = main(ej1)
      n1 = "norimlA onurB"
      n2 = "mano"
      n3 = "zlzo uCnu"
      self.assertEqual(result, n2 + n1 + n3)
      

if __name__ == '__main__':
  unittest.main()
