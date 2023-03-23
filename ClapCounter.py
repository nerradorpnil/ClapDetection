from ClapDetect import ClapListener
from gpiozero import LED
from time import sleep

light1 = LED(21)
light2 = LED(20)
light3 = LED(16)
#-------------
clapsInLine = 0
led1Status = False
led2Status = False
led3Status = False
led1ClapsNeeded = 1
led2ClapsNeeded = 2
led3ClapsNeeded = 3
stopClapsNeeded = 4
#-------------

#getters/setters
#getters/setters
def setLed1ClapsNeeded(num):    # needs integer
    global led1ClapsNeeded
    led1ClapsNeeded = int(num)
def setLed2ClapsNeeded(num):    # needs integer
    global led2ClapsNeeded
    led2ClapsNeeded = int(num)
def setLed3ClapsNeeded(num):    # needs integer
    global led3ClapsNeeded
    led3ClapsNeeded = int(num)
def setStopClapsNeeded(num):    # needs integer
    global stopClapsNeeded
    stopClapsNeeded = int(num)
def setClapsInLine(num):
    global clapsInLine
    clapsinLine = int(num)

# #getters
def getLed1Status():    # returns boolean
    global led1Status
    return led1Status
def getLed2Status():    # returns boolean
    global led2Status
    return led2Status
def getLed3Status():    # returns boolean
    global led3Status
    return led3Status
def getClapsInLine():   # returns integer
    global clapsInLine
    return clapsInLine

def flipLedStatus(LedNumStat):
    if (LedNumStat):
        LedNumStat = False
    else:
        LedNumStat = True
    return LedNumStat

#def getLedStatuses():
    #return Led1Status, Led2Status, Led3Status

def setLedStatuses():
    return

def updateLEDs(Led1, Led2, Led3):
    if Led1:
        light1.on()
    else:
        light1.off()

    if Led2:
        light2.on()
    else:
        light2.off()

    if Led3:
        light3.on()
    else:
        light3.off()
        
    return

def main():
    CDetect = ClapListener()
    oneClap = False
    global clapsInLine
    clapsInLine = 0
    global led1Status
    global led2Status
    global led3Status

    # primary loop (DO NOT TOUCH LOL)
    while(True):
        print("Listening For Claps")
        for i in range(50):
            oneClap = CDetect.listen()
            if (oneClap):
                clapsInLine = clapsInLine + 1
                oneClap = False
                i = 0

        if (clapsInLine == led1ClapsNeeded):
            led1Status = flipLedStatus(led1Status)
        if (clapsInLine == led2ClapsNeeded):
            led2Status = flipLedStatus(led2Status)
        if (clapsInLine == led3ClapsNeeded):
            led3Status = flipLedStatus(led3Status)

        sleep(1)
        updateLEDs(led1Status, led2Status, led3Status)
        print("Lights updated")
        #prevClaps = clapsInLine
        return clapsInLine
        




