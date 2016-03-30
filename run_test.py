import unittest
from sample import PyGoogleCalc 

if __name__ == '__main__':
   suite = unittest.TestLoader().loadTestsFromTestCase(PyGoogleCalc)
   result = unittest.TextTestRunner(verbosity=2).run(suite)
