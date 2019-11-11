import sys
sys.path.append('../')
from commonImports import *

allyToLock = 2;

def trigger():
    global allyToLock
    allyToLock = randint(2,5)

def hold():
    key = "f" + str(allyToLock)
    keyboard.press(key)
    keyboard.release(key)

def release():
    pass