import helperClass
reload(helperClass)
from helperClass import *
import time
import unittest

class Folders(unittest.TestCase):

    h = Helper("lab08-Homework")
    
    def setUp(self):
        self.h.openSUT()

    def tearDown(self):
        self.h.closeSUT()

    def test_apps_delete(self):
        icons = findAllList("file.png")
        number = len(icons)
        print(number)
        for i in range(2):
            dragDrop(icons[i], "blueFolder.png")
            number -= 1
            time.sleep(0.2)
            self.assertEqual(len(findAllList("file.png")), number)           
        
        dragDrop(icons[2] ,"orangeFolder.png")
        number -= 1
        time.sleep(0.2)          
        self.assertEqual(len(findAllList("file.png")), number)
        dragDrop(icons[3],"greenFolder.png")
        time.sleep(0.2)
        self.assertEqual(len(findAllList("fileCloseup.png")),number)

                                
if __name__ == '__main__':
    #suite = unittest.TestLoader().loadTestsFromModule(sys.modules[__name__])
    suite = unittest.TestLoader().loadTestsFromTestCase(Folders)
    unittest.TextTestRunner(verbosity=3).run(suite)