import sys
sys.path.append('../')
from commonImports import *

def trigger():
    rand = randint(0,len(globalVariables.items)-1)
    keyboard.press(globalVariables.items[rand])
    keyboard.release(globalVariables.items[rand])

def hold():
    pass

def release():
    pass