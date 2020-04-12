# IF YOU WANT TO RUN THE TESTS YOU MIGHT NEED TO RETAKE SOME 
# SCREENSHOTS BECAUSE OF ENVIRONMENT DIFFERENCES

import helperClass
reload(helperClass)
from helperClass import *
import time
import unittest

class Buttons(unittest.TestCase):

    h = Helper("lab08-Lab")
    
    def setUp(self):
        self.h.openSUT()

    def tearDown(self):
        self.h.closeSUT()

    def test_buttons_text(self):
        images = ["1582510089734.png","red.png","pink.png"]
        correctLines = ["Green button was clicked!", "Red button was clicked!",
                        "Pink button was clicked!"]
        for i in range(3):
            click(images[i])
            time.sleep(0.5)
            r = find("1583697429270.png")
            line = r.collectLinesText()[0]
            self.assertEqual(correctLines[i], line)

    
    def test_buttons_visible(self):
        images = ["1582510089734.png",Pattern("red.png").similar(0.98),Pattern("pink.png").exact()]
        for i in range(3):
            click(images[i])
            time.sleep(1)
            #find(images[i]).highlight(1)
            self.assertIsNotNone(exists(images[i]))  


class Editor(unittest.TestCase):

    h = Helper("Lab")
    
    def setUp(self):
        #self.h.openSUT()
        click("1581277307440-1.png")

    def tearDown(self):
        self.h.closeSUT()

    def test_editor(self): #final ver
        time.sleep(2)
        #make sure everything is closed
        if exists(Pattern("firstClosed-2.png").similar(0.92)):
            click()
            
        click(Pattern("1578417683993-1.png").targetOffset(0,50))
        type("test")
        
        copied = copyAllText()
        self.assertEqual(copied, "test")
        
        click(Pattern("firstOpen-2.png").similar(0.96))
        click()
        click(Pattern("1578417683993-1.png").targetOffset(0,50))
        
        copied = copyAllText()
        self.assertEqual(copied, "test")


class Copiable(unittest.TestCase):

    h = Helper("Lab")
    
    def setUp(self):
        self.h.openSUT()
        click("1581286649104.png")

    def tearDown(self):
        self.h.closeSUT()

    def test_copiable(self):
        time.sleep(1)
        words = self.h.reg.collectWords()    
        check = ["First", "Second", "Third", "Forth", "Fifth"]
        for i in range(len(words)):
            doubleClick(words[i])
            self.assertEqual(copySelectedText(), check[i])


class Folder(unittest.TestCase):

    h = Helper("Lab")
    
    def setUp(self):
        self.h.openSUT()
        click("1581325376798.png")

    def tearDown(self):
        self.h.closeSUT()


    def test_folder(self):
        icons = findAllList("1581790457186.png")
        number = len(icons)
        for i in range(2):
            dragDrop(icons[i], "1581790493142.png")
            number -= 1
            time.sleep(0.2)
            self.assertEqual(len(findAllList("1581790457186.png")), number)
        dragDrop("1581790457186.png", "1581790493142.png")
        self.assertEqual(len(findAllList("1581790457186.png")), number)


class Resizer(unittest.TestCase):

    h = Helper("Lab08-Lab")
    
    def setUp(self):
        self.h.openSUT()

    def tearDown(self):
        self.h.closeSUT()

    def create_reg(self):
        borders = findAllList("1581326531025.png")
        sorted_borders = sorted(borders, key=lambda m:m.x)
        reg = Region(sorted_borders[0].x + sorted_borders[0].w, 
                    sorted_borders[0].y,
                    sorted_borders[1].x - sorted_borders[0].x - sorted_borders[0].w,
                    sorted_borders[0].h)
        return reg

    def test_resizer(self):
        click("1581326295109.png")
        #resolutions = ["1583755280568.png", "1583755288711.png", "1583755295854.png"]
        resolutions = [findAllText("Desktop"), findAllText("Tablet"), findAllText("Mobile")]
        n_buttons = len(self.h.reg.findAllList("1581328241561.png"))

        for res in resolutions:
            click(res)
            time.sleep(0.2)
            reg = self.create_reg()
            reg.highlight(1)
            time.sleep(1)
            self.assertEqual(n_buttons, len(reg.findAllList("1581328241561.png"))) 
        

if __name__ == '__main__':
    #suite = unittest.TestLoader().loadTestsFromModule(sys.modules[__name__])
    suite = unittest.TestLoader().loadTestsFromTestCase(Folder)
    unittest.TextTestRunner(verbosity=3).run(suite)