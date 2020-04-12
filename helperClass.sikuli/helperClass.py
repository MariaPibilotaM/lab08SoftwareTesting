from sikuli import *
import time
import os
import HTMLTestRunner
import subprocess
import java.lang.System as JS

# make into a class with version (or app) field?

class Helper:

    def __init__(self, app):
        self.app = app
        self.proc = ""
        self.reg = ""
    
    def openSUT(self):
        appPath = os.path.dirname(getBundlePath())+"/"+self.app+".jar"
        # specify full java path instead of "java" if app doesn't open
        self.proc = subprocess.Popen(["java", "-jar", appPath])

        regImg = ""
        if self.app == "lab08-Lab":
            regImg = "1582510315250.png" # retake this screenshot if it doesn't work
        elif self.app == "lab08-Homework":
            regImg = "1583697109639.png" # retake this screenshot if it doesn't work
            
        if regImg == "":
            print("No such jar was given")
        else:
            try:
                wait(regImg, 10)  # increase wait time if your computer is slow
                time.sleep(0.5)
                self.reg = find(regImg)
            except:
                print("Can't find region or the app didn't open fast enough. Please retake" +
                      "the screenshots or increase wait time above")
            
   
    def closeSUT(self):
        if self.proc != "":
            self.proc.kill()
        else:
            print("Can't close SUT. No SUT open.")
        self.proc = ""
        time.sleep(0.5)


def createReporter(name):
    filePath = os.path.dirname(getBundlePath())+"/Report.html"
    outfile = open(filePath, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                title='Report by '+name,
                description='This a report' # add smt
                )
    return runner


def copySelectedText(): #getCopiedText
    if "win" in JS.getProperty("os.name").lower():
        keyMod = KeyModifier.CTRL # for win
    else:
        keyMod = KeyModifier.CMD # for mac/linux
    type("c", keyMod)
    return Env.getClipboard()

def copyAllText(): # getAllCopiedText
    if "win" in JS.getProperty("os.name").lower():
        keyMod = KeyModifier.CTRL # for win
    else:
        keyMod = KeyModifier.CMD # for mac/linux
    type("a", keyMod)
    type("c", keyMod)
    return Env.getClipboard()
