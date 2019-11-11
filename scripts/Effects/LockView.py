import sys
sys.path.append('../')
from commonImports import *

def trigger():
    keyboard.press("y")
    keyboard.release("y")

def hold():
    pass

def release():
    keyboard.press("y")
    keyboard.release("y")
