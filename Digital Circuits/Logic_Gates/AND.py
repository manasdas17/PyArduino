import os
import sys
cwd=os.getcwd()
(setpath_,Logic_Gates)=os.path.split(cwd)
print setpath_
(setpath,Codes)=os.path.split(setpath_)
print setpath
sys.path.append(setpath) 

from Arduino.Arduino import Arduino
from time import sleep

class AND_GATE:

    def __init__(self,baudrate):
        self.baudrate=baudrate
        self.setup()
        self.run()
        self.exit()


    def setup(self):
        self.obj_arduino=Arduino()
        self.port=self.obj_arduino.locateport()
        self.obj_arduino.open_serial(1,self.port,self.baudrate)

    def run(self):
        self.ledPin=9
        self.aPin=5
        self.bPin=6
        for _ in range(0,100):
             vala=self.obj_arduino.cmd_digital_in(1,self.aPin) #Reads state of aPin and stores it in vala
             print "A= "+vala
             #print type(vala)
             #sleep(0.1)
             valb=self.obj_arduino.cmd_digital_in(1,self.bPin) #Reads state of bPin and stores it in valb
             print "B= "+valb
             #print type(valb)
             #sleep(0.1)
             
             if vala=='1' and valb=='1':
                 self.obj_arduino.cmd_digital_out(1,self.ledPin,1) #sets state of output pin as HIGH
                 sleep(0.1)
             
             else:
                 self.obj_arduino.cmd_digital_out(1,self.ledPin,0) #sets state of output pin as LOW
                 sleep(0.1)

       


    def exit(self):
        self.obj_arduino.close_serial()

def main():
    obj_gate=AND_GATE(115200)

if __name__=='__main__':
    main()

        
