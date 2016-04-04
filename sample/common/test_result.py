import unittest
import sys

class testResult(object):
    def __init__(self, testClass):
        self.cTest = testClass
        self.outLogFile = self.cTest.get_out_path('test_result.log')

    def runTest(self, isSilent=False):
        '''
        if isSilent is False then sys.stderr will be used as output of result.
        Otherwise output will be saved to the file.
        Read documentation of TextTestRunner for more information.
        '''
        paramDic = {'stream': None, 'verbosity': 2}
        if isSilent:
           paramDic['stream'] = open(self.outLogFile, 'w')
        suite = unittest.TestLoader().loadTestsFromTestCase(self.cTest)
        self.result = unittest.TextTestRunner(**paramDic).run(suite)
        if paramDic['stream']:
           paramDic['stream'].close()
        self.checkResult(isSilent)

    def checkResult(self, isSilent=False):
        '''
        Value of isSilent is processed conversely to the runTest method.
        if isSilent is False then output will be saved to the file.
        Otherwise output will be printed to the sys.stderr.
        '''
        if self.result.wasSuccessful():
           return

        myOutFile = sys.stderr
        if not isSilent:
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
