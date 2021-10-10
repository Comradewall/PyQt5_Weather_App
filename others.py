from datetime import datetime
from pyfirmata import Arduino,util
from time import sleep 
def wTime():
    now = datetime.now()
    global h
    global m1
    h = now.hour
    m = now.minute
    if (m < 10):
        m1 = "0" + str(m)
    else: m1 = m
def connectArduino(port):
    global board
    board = Arduino(port)
    global it
    it = util.Iterator(board)
    it.start()
    sleep(1)
def AnalogRead(pin):
    board.analog[pin].enable_reporting()
    sleep(1)
    global analogval
    analogv = board.analog[pin].read()
    analogval = analogv * 5