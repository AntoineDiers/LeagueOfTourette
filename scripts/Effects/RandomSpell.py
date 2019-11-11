import sys
sys.path.append('../')
from commonImports import *

def trigger():
    rand = randint(0,2)
    keyboard.press(globalVariables.spells[rand])
    keyboard.release(globalVariables.spells[rand])

def hold():
    pass

def release():
    pass