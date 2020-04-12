import helperClass
reload(helperClass)
from helperClass import *
import time
import unittest

class TAB_NAME(unittest.TestCase):

    h = Helper("lab08-Lab")  # name of the jar
    
    def setUp(self):
        self.h.openSUT()
        #click(*tab that you want to open*)
        time.sleep(0.2)

    def tearDown(self):
        self.h.closeSUT()

    def test_name(self):
         #....

    def test_name2(self):
        #...

#...
     
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TAB_NAME)
    unittest.TextTestRunner(verbosity=3).run(suite)
    #reporter = createReporter(NAME)
    #reporter.run(suite)