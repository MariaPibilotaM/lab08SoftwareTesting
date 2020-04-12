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
        time.sleep(0.2)
        self.assertEqual(line[0].text(),"6")
    def test_calc_err(self):
        r= Region(Region(660,218,212,36))
        click("1586701381521.png")
        click("1586701387587.png")
        click("1586701396607.png")
        print(r.text())
        time.sleep(0.2)
        self.assertEqual(r.text(),"Error")
       
class PinCode(unittest.TestCase):

    h = Helper("lab08-Homework")
    
    def setUp(self):
        self.h.openSUT()
        click("1586701809039.png")

    def tearDown(self):
        self.h.closeSUT()  
        
    def test_pin_x(self):
        r= Region(Region(703,226,132,35))
        for i in range(4):
            click("1586701945860.png")
            time.sleep(0.2)
            self.assertEqual(r.text(),"X"*(i+1))
        
    def test_pin_unlock(self):
        click("1586702294779.png")
        click("1586702304332.png")
        click("1586702314867.png")
        click("1586702324802.png")
        time.sleep(0.5)
        r=Region(Region(490,170,554,424))

        self.assertIn("Welcome,", r.text())
        self.assertIn("!", r.text())
        
    def test_pin_lock(self): 
         r= Region(Region(703,226,132,35))
         
         for i in range(4):
 
             click("1586701945860.png")
         self.assertIsNotNone(exists("1586703233026.png"))
        

class Converter(unittest.TestCase):

    h = Helper("lab08-Homework")

    def setUp(self):
        self.h.openSUT()
        click("1586707072311.png")

    def tearDown(self):
        self.h.closeSUT()

    def test_text2uni(self):
        r1 = Region(Region(664,271,296,395))
        r1.click()
        type("a")

        r2 = Region(Region(959,291,294,370))
        r2.click()
        copied = copyAllText()
        self.assertTrue(copied.strip().isdigit())

    def test_fields(self):
        
        r = Region(Region(669,295,292,367))
        r.click()
        type("a")

        r = Region(Region(959,294,290,388))
        r.click()
        copied = copyAllText()
        type("a")
        copied2 = copyAllText()
        self.assertEqual(copied, copied2)

    def test_switch(self):
        r = Region(Region(662,236,596,443))
        boxes = r.find("1586715313979.png")
        location_boxes = boxes.getTarget()
        button = r.find("1586714611982.png")
        location = button.getTarget()
        
        click("1586714611982.png")
        boxes2 = r.find("1586715313979.png")
        location_boxes2 = boxes2.getTarget()

        button2 = r.find("1586714611982.png")
        location2 = button2.getTarget()

        print(location_boxes)
        print(location_boxes2)
        
        print(location)
        print(location2)
        
        self.assertEqual(location_boxes, location_boxes2)
        self.assertEqual(location, location2)

    def test_uni2text(self):
        click("1586714611982.png")
        r = Region(Region(661,295,298,371))
        r.click()
        type("97")
        r2 = Region(Region(953,288,299,367))
        r2.click()
        copied = copyAllText()
        self.assertTrue(copied.strip().isalpha())

        r.click()
        type("yy")
        r2.click()
        copied = copyAllText()
        self.assertEqual("Error! Not unicode.", copied)

class CatFlower(unittest.TestCase):

    h = Helper("lab08-Homework")

    def setUp(self):
        self.h.openSUT()
        click("1586716932321.png")

    def tearDown(self):
        self.h.closeSUT()

    def test_place_cat(self):
        r = Region(Region(1136,344,119,330))
        r_lanes = Region(Region(660,338,467,356))
        if(r.exists("1586717517431.png")):
            click("1586717517431.png")
            click("1586717543250.png")
            cat = r_lanes.exists("1586717517431.png")
            self.assertIsNotNone(cat)
    
        elif(r.exists("1586718423976.png")):
            click("1586718423976.png")
            click("1586717543250.png")
            cat = r_lanes.exists("1586718423976.png")
            self.assertIsNotNone(cat)

        elif(r.exists("1586718681140.png")): 
            click("1586718681140.png")
            click("1586717543250.png")
            cat = r_lanes.exists("1586718681140.png")
            self.assertIsNotNone(cat)  

    def test_cat_moves(self):
        r = Region(Region(1136,344,119,330))
        r_lanes = Region(Region(657,339,474,356))
        if(r.exists("1586717517431.png")):
            click("1586717517431.png")
            click("1586717543250.png")
            locations = []
            results = []

            for i in range(5):
                cat = r_lanes.exists("1586717517431.png")
                location = cat.getTarget()
                locations.append(location)
                wait(1)

            for i in range(4):
                spacing = locations[i].x - locations[i+1].x
                results.append(spacing)

            self.assertEqual(results[0], results[1], results[2]) #I only compare the first 3 because Sikuli does not let me compare more
            
        elif(r.exists("1586718423976.png")):
            click("1586718423976.png")
            click("1586717543250.png")
            locations = []
            results = []

            for i in range(5): 
                cat = r_lanes.exists("1586718423976.png")
                location = cat.getTarget()
                locations.append(location)
                wait(1)

            for i in range(4):
                spacing = locations[i].x - locations[i+1].x
                results.append(spacing)

            print(results[0])
            self.assertEqual(results[0], results[1], results[2])
            

        elif(r.exists("1586718681140.png")): 
            click("1586718681140.png")
            click("1586717543250.png")
            locations = []
            results = []

            for i in range(5):  
                cat = r_lanes.exists("1586718681140.png")
                location = cat.getTarget()
                locations.append(location)
                wait(1)

            for i in range(4):
                spacing = locations[i].x - locations[i+1].x
                results.append(spacing)

            self.assertEqual(results[0], results[1], results[2])
            
    def test_flower_gone(self):
        r = Region(Region(1134,303,123,385))
        r_lanes = Region(Region(657,318,473,379))
        if(r.exists("1586717517431.png")):
            flowers = findAllList(Pattern("1586730155813.png").similar(0.80))
            click("1586717517431.png")
            click("1586717543250.png")
            wait(10)
            self.assertEqual(len(flowers), len(findAllList(Pattern("1586730155813.png").similar(0.83))))
            
        elif(r.exists("1586718423976.png")):
            flowers = findAllList(Pattern("1586730155813.png").similar(0.80))
            click("1586718423976.png")
            click("1586717543250.png")
            wait(10)
            self.assertEqual(len(flowers), len(findAllList(Pattern("1586730155813.png").similar(0.80))))
        elif(r.exists("1586718681140.png")):
            flowers = findAllList(Pattern("1586730155813.png").similar(0.80))
            click("1586718681140.png")
            click("1586717543250.png")
            wait(10)
            self.assertNotEqual(len(flowers), len(findAllList(Pattern("1586730155813.png").similar(0.80))))
            
    def test_cats_win(self):
        r = Region(Region(1136,344,119,330))
        r_lanes = Region(Region(657,339,474,356))
        if(r.exists("1586717517431.png")):
            click("1586717517431.png")
            click("1586717543250.png")
            wait(3)
            self.assertIsNone(exists("1586730741040.png"))
            
        elif(r.exists("1586718423976.png")):
            click("1586718423976.png")
            click("1586717543250.png")
            wait(3)
            self.assertIsNone(exists("1586730741040.png"))
        elif(r.exists("1586718681140.png")):
            click("1586718681140.png")
            click("1586717543250.png")
            wait(3)
            self.assertIsNone(exists("1586730741040.png"))   

    def test_cat_backup(self):
        r = Region(Region(1135,315,122,377))
        r_lanes = Region(Region(661,342,466,351))
        
        if(r.exists("1586717517431.png")):
            click("1586717517431.png")
            click("1586717543250.png")
            wait(3)

            orange_cat = r.findAllList("1586717517431.png")
            gray_cat = r.findAllList("1586718681140.png")
            white_cat = r.findAllList("1586718423976.png")
            
            self.assertEqual(2, (len(orange_cat) + len(gray_cat) + len(white_cat)))
            
        elif(r.exists("1586718423976.png")):
            click("1586718423976.png")
            click("1586717543250.png")
            wait(3)

            orange_cat = r.findAllList("1586717517431.png")
            gray_cat = r.findAllList("1586718681140.png")
            white_cat = r.findAllList("1586718423976.png")
            
            self.assertEqual(2, (len(orange_cat) + len(gray_cat) + len(white_cat)))            
        elif(r.exists("1586718681140.png")):
            click("1586718681140.png")
            click("1586717543250.png")
            wait(3)
            orange_cat = r.findAllList("1586717517431.png")
            gray_cat = r.findAllList("1586718681140.png")
            white_cat = r.findAllList("1586718423976.png")
            
            self.assertEqual(2, (len(orange_cat) + len(gray_cat) + len(white_cat)))               
            
                                 
if __name__ == '__main__':
    #suite = unittest.TestLoader().loadTestsFromModule(sys.modules[__name__])
   # suite = unittest.TestLoader().loadTestsFromTestCase(Folders)
 #   suite = unittest.TestLoader().loadTestsFromTestCase(Calculator)
 #suite = unittest.TestLoader().loadTestsFromTestCase(PinCode)
    suite = unittest.TestLoader().loadTestsFromTestCase(Converter)
    #suite = unittest.TestLoader().loadTestsFromTestCase(CatFlower)
    unittest.TextTestRunner(verbosity=3).run(suite)