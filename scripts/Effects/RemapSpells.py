import sys
sys.path.append('../')
from commonImports import *

def trigger():
    randomizedSpells = copy(globalVariables.spells)
    shuffle(randomizedSpells)
    for i in range(len(globalVariables.spells)):
        print(globalVariables.spells[i],randomizedSpells[i])
        keyboard.remap_key(globalVariables.spells[i],randomizedSpells[i])

def hold():
    pass

def release():
    for i in range(len(globalVariables.spells)):
        keyboard.unremap_key(globalVariables.spells[i])
