import io
import unittest.mock
from main import main

class Test(unittest.TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_ex(self, mock_stdout):
      #* Test OK - 1
      r1 = main("a")
      r2 = main("u")
      r3 = main("k")
      r4 = main("kaa")
      r5 = main("")
      
      self.assertEqual(r1, "a es una vocal")
      self.assertEqual(r2, "u es una vocal")
      self.assertEqual(r3, "k es una consonante")
      self.assertEqual(r4, "ERROR")
      self.assertEqual(r5, "ERROR")
      

if __name__ == '__main__':
  unittest.main()
