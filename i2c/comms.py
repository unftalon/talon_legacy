import smbus
import time
    # for RPI version 1, use "bus = smbus.SMBus(0)"
bus = smbus.SMBus()
    # This is the address we setup in the Arduino Program
address = 0x04

def writeNumber(value, address):
    bus.write_byte(address, value)
    # bus.write_byte_data(address, value)
    return -1

def writeChar(address, value):
    bus.write_word_data(address, value)
    return -1


def readNumber(address):
    number = bus.read_byte(address)
    #number = bus.read_byte_data(address, 1)
    return number
print dir(smbus.SMBus)
while True:
    var = input("Enter a Number: ")
    if not var:
       continue

    writeNumber(address,var)
    print "RPI: Hi Arduino, I sent you ", var


    # sleep one second
    time.sleep(1)

        #number = readNumber(address)
        #print "Arduino: Hey RPI, I received a digit ", number
   #     print


    
def rdb():
   buffer[10]
   bus.read_block_data(address,buffer)
