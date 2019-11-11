import sys
sys.path.append('../')
from commonImports import *

def trigger():
    summs = globalVariables.summs
    keyboard.remap_key(summs[0],summs[1])
    keyboard.remap_key(summs[1],summs[0])

def hold():
    pass

def release():
    summs = globalVariables.summs
    keyboard.unremap_key(summs[0])
    keyboard.unremap_key(summs[1])