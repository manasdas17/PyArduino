
import os
import sys
cwd=os.getcwd()
(setpath_,Trials)=os.path.split(cwd)
print setpath_
(setpath,Codes)=os.path.split(setpath_)
print setpath
sys.path.append(setpath) 

from Arduino._Arduino_ import _Arduino_
#from Arduino.IC_methods import IC_methods
from time import sleep

class Trial:

    
    
    def __init__(self,baudrate):
        self.baudrate=baudrate
        self.setup()
        self.run()
        self.exit()


    def setup(self):
        
        self.obj_arduino=_Arduino_()
        self.port=self.obj_arduino.locateport()
        self.obj_arduino.open_serial(1,self.port,self.baudrate)

        #self.obj_icm=IC_methods(self.baudrate,self.port)

    def run(self):

        dataPin=9
        clockPin=10
        latchPin=11

        ledPin=5 #LED that shows serial output
        clockLed=6 #LED that shows clock pulses

        self.obj_arduino.cmd_digital_out(1,latchPin,1) #parallel load mode

        for _ in range(0,50):
            print ("Give input, Parallel load mode:")
            sleep(2)
            self.obj_arduino.cmd_digital_out(1,clockPin,1) #positive edge occurs
                                                           #parallel load is stored
            print("Inputs stored, Serial shift mode:")
            sleep(0.5)

            self.obj_arduino.cmd_digital_out(1,clockPin,0)
            self.obj_arduino.cmd_digital_out(1,latchPin,0) #serial out mode

            self.obj_arduino.cmd_shift_in(dataPin,clockPin,ledPin,clockLed)

            self.obj_arduino.cmd_digital_out(1,latchPin,1)
            self.obj_arduino.cmd_digital_out(1,ledPin,0)

    

    


def main():
    piso=Trial(115200)

if __name__=='__main__':
    main()
  
