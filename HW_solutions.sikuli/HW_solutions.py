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

    def test_move_folders(self):
        dragDrop("blueFolder.png","greenFolder.png")
        self.assertIsNotNone(exists( "blueOnGreen.png"))
        dragDrop("blueFolder.png","orangeFolder.png")
        self.assertIsNotNone(exists( "blueOnOrange.png"))
        dragDrop("greenFolder.png","blueFolder.png")
        self.assertIsNotNone(exists( "greenFolder.png"))
        
    def test_menu(self):
        r = Region(Region(469,157,597,462))
        
        dragDrop("blueFolder.png",Location(r.x,r.y+40))
        rightClick("closeUp.PNG")
        time.sleep(0.2)

        
class Calculator(unittest.TestCase):

    h = Helper("lab08-Homework")
    
    def setUp(self):
        self.h.openSUT()
        click("1586688902569.png")

    def tearDown(self):
        self.h.closeSUT()

    def test_acalc_black(self):
        time.sleep(0.2)
        self.assertIsNotNone(exists( "empty.png"))

        click("1586689013605.png")
        time.sleep(0.2)
        self.assertIsNotNone(exists( "1586689977446.png"))
        for i in range(2): 
           click("1586689474885.png")
        time.sleep(0.2)
        r = Region(Region(641,265,264,66))
        #self.assertIsNotNone(exists( "1586690905053.png"))


        
        
        
        

        

                                
if __name__ == '__main__':
    #suite = unittest.TestLoader().loadTestsFromModule(sys.modules[__name__])
    suite = unittest.TestLoader().loadTestsFromTestCase(Folders)
    #suite = unittest.TestLoader().loadTestsFromTestCase(Calculator)
    unittest.TextTestRunner(verbosity=3).run(suite)