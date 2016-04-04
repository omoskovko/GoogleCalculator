import unittest

class testResult(object):
    def __init__(self, testClass):
        self.cTest = testClass
        self.outLogFile = self.cTest.get_out_folder('output.log', 'test_result.log')

    def runTest(self):
        #myOutFile = open(self.outLogFile, 'w')
        suite = unittest.TestLoader().loadTestsFromTestCase(self.cTest)
        self.result = unittest.TextTestRunner(verbosity=2).run(suite)
        #self.result = unittest.TextTestRunner(stream=myOutFile, verbosity=2).run(suite)
        #myOutFile.close()
        #self.checkResult()

    def checkResult(self):
        if self.result.wasSuccessful():
           return

        myOutFile = open(self.outLogFile, 'w')
        if self.result.errors:
           print('ERRORS:', sep='\n', end='\n', file=myOutFile)
        for r in self.result.errors:
           print(*r, sep='\n', end='\n', file=myOutFile)

        if self.result.failures:
           print('FAILURES:', sep='\n', end='\n', file=myOutFile)
        for r in self.result.failures:
           print(*r, sep='\n', end='\n', file=myOutFile)
        myOutFile.close()
