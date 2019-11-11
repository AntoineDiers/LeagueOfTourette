import sys
sys.path.append('../')
from commonImports import *

def trigger():
    pass

def hold():
    keyboard.press("ctrl")
    keyboard.press("\"")
    keyboard.release("\"")
    keyboard.release("ctrl")

def release():
    pass