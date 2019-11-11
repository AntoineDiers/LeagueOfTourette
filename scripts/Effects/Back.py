import sys
sys.path.append('../')
from commonImports import *

def mouseEvent(event):
    if(type(event) == mouse.ButtonEvent):
        globalVariables.mouseMoved = True

mouse.hook(mouseEvent)

def trigger():
    for item in globalVariables.items:
        keyboard.block_key(item)
    for spell in globalVariables.spells:
        keyboard.block_key(spell)
    for summ in globalVariables.summs:
        keyboard.block_key(summ)

def hold():
    keyboard.press("b")
    keyboard.release("b")

def release():
    for item in globalVariables.items:
        keyboard.unblock_key(item)
    for spell in globalVariables.spells:
        keyboard.unblock_key(spell)
    for summ in globalVariables.summs:
        keyboard.unblock_key(summ)

