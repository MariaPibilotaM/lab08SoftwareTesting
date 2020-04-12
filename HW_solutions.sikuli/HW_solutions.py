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
        r = Region(Region(474,168,586,445))
        
        dragDrop("blueFolder.png",Location(r.x,r.y+70))
        rightClick("closeUp.PNG")
        #rightClick(Location(r.x+10,r.y+40))
        print(r.text())
        time.sleep(0.2)
        lines = r.collectLines()
        words = ["Copy","Paste","Search on Bing"]
        for i in range(len(lines)):
            uprint(lines[i].text())

        
class Calculator(unittest.TestCase):

    h = Helper("lab08-Homework")
    
    def setUp(self):
        self.h.openSUT()
        click("1586688902569.png")

    def tearDown(self):
        self.h.closeSUT()

    def test_acalc_black(self):
        time.sleep(0.2)
        #r = Region(Region(696,261,267,62))
        r = Region(Region(659,279,219,35))

        self.assertEqual(r.text(),"")
        click("1586689013605.png")
        time.sleep(0.2)
        self.assertEqual(r.text(),"1")
        time.sleep(0.2)
        for i in range(21): 
           click("1586689474885.png")
        time.sleep(0.2)        
        self.assertEqual(len(r.text()),20)
        
    def test_calc_purple(self):
        r= Region(Region(660,218,212,36))
        line = r.collectLines()
        self.assertEqual(line[0].text(),"0")
        click("1586700817916.png")
        click("1586700831339.png")
        click("1586700817916.png")
        self.assertEqual(line[0].text(),"4")
        for i in range(3):
            click("1586700969420.png")
        click("1586700817916.png")
        click("1586701009475.png")
        click("1586701021899.png")
        click("1586700831339.png")
        self.assertEqual(line[0].text(),"6")
    def test_calc_err(self):
        r= Region(Region(660,218,212,36))
        click("1586701381521.png")
        click("1586701387587.png")
        click("1586701396607.png")
        print(r.text())
        self.assertEqual(r.text(),"Error")
       
        
        

       

        
        
        
        

        

                                
if __name__ == '__main__':
    #suite = unittest.TestLoader().loadTestsFromModule(sys.modules[__name__])
   # suite = unittest.TestLoader().loadTestsFromTestCase(Folders)
    suite = unittest.TestLoader().loadTestsFromTestCase(Calculator)
    unittest.TextTestRunner(verbosity=3).run(suite)