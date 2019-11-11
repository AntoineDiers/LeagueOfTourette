import sys
sys.path.append('../')
from commonImports import *

vomiId = 0

def trigger():
    pass

def hold():
    global vomiId
    vomiKey = "f" + str((vomiId%3)+2)
    vomiId += 1
    keyboard.press(vomiKey)
    keyboard.release(vomiKey)

def release():
    pass
