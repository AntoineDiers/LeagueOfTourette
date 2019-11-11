from commonImports import *
from EffectTrigger import *
import xml.etree.ElementTree as ET

from Effects import RemapSpells
from Effects import RemapSummoners
from Effects import Flash
from Effects import LockView
from Effects import Dance
from Effects import Puke
from Effects import LockOnAlly
from Effects import SwapPlayers
from Effects import RandomSpell
from Effects import RandomItem
from Effects import Zoom
from Effects import Back


def loadConfig(filename,effectsList):
    tree = ET.parse(filename)
    root = tree.getroot()

    seed(int(root.find("seed").text))

    globalVariables.TICK_PERIOD = float(root.find("tick_period").text)

    globalVariables.flash_key = root.find("flash_key").text

    effects = root.find("effects")
    for effect in effects:
        effectClass = effect.tag

        trigger = eval(effectClass + ".trigger")
        hold = eval(effectClass + ".hold")
        release = eval(effectClass + ".release")

        resetFlag = effect.attrib["reset_flag"]

        period = float(effect.attrib["period"])
        period_sigma = float(effect.attrib["period_sigma"])
        duration = float(effect.attrib["duration"])
        duration_sigma = float(effect.attrib["duration_sigma"])
        effectsList.append(EffectTrigger(effectClass,trigger,hold,release,duration,duration_sigma,period,period_sigma,resetFlag))

effects = []
loadConfig("../config/config.xml",effects)

while(True):
    sleep(globalVariables.TICK_PERIOD)
    triggerActivated = False
    for trigger in effects:
        if(trigger.activated):
            triggerActivated = True

    for trigger in effects:
        if(trigger.activated or not triggerActivated):
            trigger.tick()
            if(trigger.activated):
                triggerActivated = True

