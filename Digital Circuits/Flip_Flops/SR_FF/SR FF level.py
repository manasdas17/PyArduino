import os
import sys
cwd=os.getcwd()
(setpath__,SR_FF)=os.path.split(cwd)
print setpath__
(setpath_,Codes)=os.path.split(setpath__)
print setpath_
(setpath,Codes)=os.path.split(setpath_)
print setpath
sys.path.append(setpath) 

from Arduino.Arduino import Arduino
from time import sleep

class SR_FF:

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

        self.S='0'
        self.R='0'

        self.sPin=5 #Input S is given to Pin 5
        self.rPin=6 #Input R is given to Pin 6

        #assuming initial state:
        self.Q='0'
        self.Qbar='1'

        self.qPin=9
        self.qbarPin=10

        self.clockPin=2 #external clock


        for _ in range(0,500):

            if self.Q=='0':
                self.obj_arduino.cmd_digital_out(1,self.qPin,0) #Gives low output at Q
            elif self.Q=='1':
                self.obj_arduino.cmd_digital_out(1,self.qPin,1) #Gives high output at Q
            else:
                pass
            sleep(0.1)   
            if self.Qbar=='0':
                self.obj_arduino.cmd_digital_out(1,self.qbarPin,0) #Gives low output at Qbar
            elif self.Qbar=='1':
                self.obj_arduino.cmd_digital_out(1,self.qbarPin,1) #Gives high output at Qbar
            else:
                pass
            sleep(0.1)

            self.S=self.obj_arduino.cmd_digital_in(1,self.sPin) #Reads the input S
            self.R=self.obj_arduino.cmd_digital_in(1,self.rPin) #Reads the input R

            if self.obj_arduino.cmd_digital_in(1,self.clockPin)=='1':

                if self.S=='0' and self.R=='1':
                    self.Q='0'
                    self.Qbar='1'
                elif self.S=='1' and self.R=='0':
                    self.Q='1'
                    self.Qbar='0'
                elif self.S=='1' and self.R=='1': #we assume this case doesn't occur
                    self.Q='0'
                    self.Qbar='0'
                else:
                    pass
                







    def exit(self):
        self.obj_arduino.close_serial()

def main():
    obj_srff=SR_FF(115200)

if __name__=='__main__':
    main()
  
