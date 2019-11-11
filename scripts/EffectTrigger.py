from commonImports import *

triggerSound = "../media/bwahaha.mp3"

class EffectTrigger():
    def __init__(self, name, triggerFunc, holdFunc, unTriggerFunc, durationMean, durationSigma, periodMean, periodSigma, resetFlag):
        self.name = name
        self.triggerFunc = triggerFunc
        self.holdFunc = holdFunc
        self.unTriggerFunc = unTriggerFunc
        self.activated = False
        self.time = 0
        self.switchTime = normalvariate(periodMean, periodSigma)
        self.durationMean = durationMean
        self.durationSigma = durationSigma
        self.periodMean = periodMean
        self.periodSigma = periodSigma
        self.resetFlag = resetFlag

    def tick(self):
        self.time += globalVariables.TICK_PERIOD

        if(self.resetFlag):
            if(eval("globalVariables." + self.resetFlag) and self.activated):
                self.time = 0
                exec("globalVariables." + self.resetFlag + " = False")

        if self.time > self.switchTime:
            if self.activated:
                print(self.name," off")
                self.unTriggerFunc()
                self.activated = False
                self.time = 0
                self.switchTime = normalvariate(self.periodMean,self.periodSigma)
            else:
                print(self.name," on")
                playsound(triggerSound)
                self.triggerFunc()
                self.activated = True
                self.time = 0
                self.switchTime = normalvariate(self.durationMean,self.durationSigma)
        else:
            if self.activated:
                self.holdFunc()