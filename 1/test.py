import io
import unittest.mock
from main import main

class Test(unittest.TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_ex(self, mock_stdout):

      #* Test OK - 1
      inputs = iter([6, "Joe", 100.99, False])
      with unittest.mock.patch('builtins.input', side_effect=lambda y: next(inputs)):
        main()
        results = mock_stdout.getvalue().splitlines()
        self.assertEqual(results[0], "Orden #6 - Joe - $100 (Propina: $10.10) - Pago: False")
      
      #* Test OK - 2
      inputs = iter([12000, "Mateo", 6000.7, True])
      with unittest.mock.patch('builtins.input', side_effect=lambda y: next(inputs)):
        main()
        results = mock_stdout.getvalue().splitlines()
        self.assertEqual(results[1], "Orden #12000 - Mateo - $6000 (Propina: $600.07) - Pago: True")
      
      #* Test Error - 1
      with self.assertRaises(ValueError):
        inputs = iter(["hola", "Mateo", 6000.7, True])
        with unittest.mock.patch('builtins.input', side_effect=lambda y: next(inputs)):
          main()

      #* Test Error - 2
      with self.assertRaises(ValueError):
        inputs = iter([12000, "Mateo", "a880", True])
        with unittest.mock.patch('builtins.input', side_effect=lambda y: next(inputs)):
          main()

if __name__ == '__main__':
  unittest.main()
