import sys
sys.path.append('../')
from commonImports import *

def trigger():
    keyboard.press(globalVariables.flash_key)
    keyboard.release(globalVariables.flash_key)

def hold():
    pass

def release():
    pass