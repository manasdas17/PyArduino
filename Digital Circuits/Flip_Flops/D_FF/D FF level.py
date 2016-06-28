import os
import sys
cwd=os.getcwd()
(setpath__,D_FF)=os.path.split(cwd)
print setpath__
(setpath_,Codes)=os.path.split(setpath__)
print setpath_
(setpath,Codes)=os.path.split(setpath_)
print setpath
sys.path.append(setpath) 

from Arduino.Arduino import Arduino
from time import sleep

class D_FF:

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

        self.D='0'
        
        self.dPin=5
        
        #assuming initial state:
        self.Q='0'
        self.Qbar='1'

        self.qPin=9
        self.qbarPin=10

        self.clockPin=2 #external clock


        for _ in range(0,500):

            if self.Q=='0':
                self.obj_arduino.cmd_digital_out(1,self.qPin,0)
                self.obj_arduino.cmd_digital_out(1,self.qbarPin,1)
                sleep(0.1)
            else:
                self.obj_arduino.cmd_digital_out(1,self.qPin,1)
                self.obj_arduino.cmd_digital_out(1,self.qbarPin,0)
                sleep(0.1)


            if self.obj_arduino.cmd_digital_in(1,self.clockPin)=='1': #Reads clock and executes when it is HIGH

                self.D=self.obj_arduino.cmd_digital_in(1,self.dPin) #Reads input D

                if self.D=='0':
                    self.Q='0'
                else:
                    self.Q='1'
                


    def exit(self):
        self.obj_arduino.close_serial()

def main():
    obj_dff=D_FF(115200)

if __name__=='__main__':
    main()
  
