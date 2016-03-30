import unittest
from . import PyGoogleCalc 

suite = unittest.TestLoader().loadTestsFromTestCase(PyGoogleCalc)
result = unittest.TextTestRunner(verbosity=2).run(suite)
