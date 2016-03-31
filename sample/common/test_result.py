import unittest

class testResult(object):
    def __init__(self, testClass):
        self.cTest = testClass

    def runTest(self):
        suite = unittest.TestLoader().loadTestsFromTestCase(self.cTest)
        self.result = unittest.TextTestRunner(verbosity=2).run(suite)

    def checkResult(self):
        if not self.result.wasSuccessful():
           self.print_disp_errors(self.result)
