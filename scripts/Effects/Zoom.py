import sys
sys.path.append('../')
from commonImports import *

def trigger():
    keyboard.press("y")
    keyboard.release("y")

def hold():
    mouse.wheel(1)

def release():
    keyboard.press("y")
    keyboard.release("y")