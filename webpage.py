import justpy as jp
from ClapCounter import main, getClapsInLine, getLed1Status, getLed2Status, getLed3Status
from ClapCounter import setStopClapsNeeded, setLed1ClapsNeeded, setLed2ClapsNeeded, setLed3ClapsNeeded
from ClapCounter import led1ClapsNeeded, led2ClapsNeeded, led3ClapsNeeded


def listen(self, msg):
    self.text = 'Listening....'
    clapsInLine = main()
    self.text = f'Detected Claps: {clapsInLine}'

def updates1(self, msg):
    setLed1ClapsNeeded(self.value)

def updates2(self, msg):
    setLed2ClapsNeeded(self.value)

def updates3(self, msg):
    setLed3ClapsNeeded(self.value)

def LED1Status(self, msg):
    ledStatus = False
    ledStatus = getLed1Status()
    if (ledStatus):
        msg = "ON"
    else:
        msg = "OFF"
    self.text = msg

def LED2Status(self, msg):
    ledStatus = False
    ledStatus = getLed2Status()
    if (ledStatus):
        msg = "ON"
    else:
        msg = "OFF"
    self.text = msg

def LED3Status(self, msg):
    ledStatus = False
    ledStatus = getLed3Status()
    if (ledStatus):
        msg = "ON"
    else:
        msg = "OFF"
    self.text = msg

def status(self, msg, index):
    ledStatus = False
    if (index == 0):
        ledStatus = getLed1Status()
    if (index == 1):
        ledStatus = getLed2Status()
    if (index == 2):
        ledStatus = getLed3Status()
    
    if (ledStatus):
        msg = "ON"
    else:
        msg = "OFF"
    self.text = msg


def project():
    wp = jp.WebPage()
    h1 = jp.Div(text='GROUP 2 FINAL- Light Clapper', classes = 'text-2xl p-2 bold', a=wp)

    configurations = ['1', '2', '3', '4', '5', '6']
    leds = ['LED1', 'LED2', 'LED3']
    statuses = ['on', 'off']

    select1 = jp.Select (value='1', classes='w-32 text-xl m-4 p-2 bg-blue  border rounded', a=wp, change=updates1)
    for configuration in configurations:
        select1.add(jp.Option(value=configuration, text=configuration))

    select2 = jp.Select (value='2', classes='w-32 text-xl m-4 p-2 bg-blue  border rounded', a=wp, change=updates2)
    for configuration in configurations:
        select2.add(jp.Option(value=configuration, text=configuration))

    select3 = jp.Select (value='3', classes='w-32 text-xl m-4 p-2 bg-blue  border rounded', a=wp, change=updates3)
    for configuration in configurations:
        select3.add(jp.Option(value=configuration, text=configuration))
    
    start = jp.Button(text = 'START', a=wp, classes='w-60 text-xl m-2 p-1 bg-blue-500 text-white', click = listen)
    clapsInLine = 0
    clapsInLine = getClapsInLine
   
    division = jp.Div()

    header = jp.Div(text='LED Status', classes='text-2xl p-2 strong', a=wp)
    jp.Span(text='LED1', classes ='text-2xl p-2', a=wp)
    viewStatus1 = jp.Button(text = 'View Status', a=wp, classes='w-36 text-xl m-2 p-1 bg-blue-500 text-white', click = LED1Status)
    jp.Span(text='LED2', classes ='text-2xl p-2', a=wp)
    viewStatus2 = jp.Button(text = 'View Status', a=wp, classes='w-36 text-xl m-2 p-1 bg-blue-500 text-white', click = LED2Status)
    jp.Span(text='LED3', classes ='text-2xl p-2', a=wp)
    viewStatus3 = jp.Button(text = 'View Status', a=wp, classes='w-36 text-xl m-2 p-1 bg-blue-500 text-white', click = LED3Status)

    return wp

jp.justpy(project)
