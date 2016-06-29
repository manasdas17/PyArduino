#3 bit SISO shift register
#in a SISO shift register, input is given to the MSB
#it shifts rightwards with positive clock pulses and output is seen at LSB

import os
import sys
cwd=os.getcwd()
(setpath_,Registers)=os.path.split(cwd)
print setpath_
(setpath,Codes)=os.path.split(setpath_)
print setpath
sys.path.append(setpath) 

from Arduino.Arduino import Arduino
from time import sleep

class SISO:

    
    
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

        pinstate='0' 
        lastpinstate='0'

        D2='0' #serial data input to FF2 (MSB FF)
        D1='0' #D1=Q2, output of FF2=input of FF1 (middle bit FF)
        D0='0' #D0=Q1, output of FF1=input of FF0 (LSB FF)

        Q='0' #serial data out, output of FF0

        #Serial input
        inPin=5

        #Serial output
        outPin=9

        #external clock pulse
        clockPin=2
        


        for _ in range(0,500):
            
            if D0=='0':
                self.obj_arduino.cmd_digital_out(1,outPin,0)
                sleep(0.1)
            else:
                self.obj_arduino.cmd_digital_out(1,outPin,1)
                sleep(0.1)

            pinstate=self.obj_arduino.cmd_digital_in(1,clockPin) #reads the state of clock

            #clock is common for all FFs
            #thus only 1 if statement for detecting positive edge of clock

            if pinstate!=lastpinstate:
                if pinstate=='1':

                    #order of FFs: FF2-FF1-FF0-serial output

                    #FF0 (LSB FF, i.e. third FF)
                    if D0=='0':
                        Q='0'
                    else:
                        Q='1'

                    #FF1 (middle bit FF i.e. second FF)
                    if D1=='0':
                        D0='0'
                    else:
                        D0='1'

                    #FF2 (MSB FF i.e first FF)
                    if D2=='0':
                        D1='0'
                    else:
                        D1='1'

                    D2=self.obj_arduino.cmd_digital_in(1,inPin) #input is given to D of FF2 (MSB FF)
                sleep(0.05)
            lastpinstate=pinstate
                    
                    
            



    def exit(self):
        self.obj_arduino.close_serial()

def main():
    siso=SISO(115200)

if __name__=='__main__':
    main()
  
