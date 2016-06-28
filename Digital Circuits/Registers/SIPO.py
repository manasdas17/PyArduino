#3 bit SIPO shift register using D FFs
#input by user is given to FF2 (MSB FF).
#It then shifts rightwards serially and is eventually lost through
#FF0 (LSB FF) after 3 clock pulses
#outputs of all FFs (all bits) are obtained at all instances 

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

class SIPO:

    
    
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

        clockPin=5 # Pulse to be counted

        D2='0' #serial data input, input by user is given to FF2 (MSB FF)
                #output of FF2=input of FF1
        D1='0' #D1=Q2, FF1 (middle bit FF), output of FF1=input of FF0
        D0='0' #D0=Q1, FF0 (LSB FF), output of FF0 = Q0

        Q='0' #output of FF0

        #Serial input
        inPin=5

        #Parallel output
        outPin1=9 #LSB = Q
        outPin2=10 #middle bit
        outPin3=11 #MSB

        #external clock pulse
        clockPin=2
        


        for _ in range(0,100):

            #pin 9=Q=LSB
            if D0=='0':
                self.obj_arduino.cmd_digital_out(1,outPin1,0)
                sleep(0.1)
            else:
                self.obj_arduino.cmd_digital_out(1,outPin1,1)
                sleep(0.1)

            #pin 10=Q1=D0=middle bit
            if D1=='0':
                self.obj_arduino.cmd_digital_out(1,outPin2,0)
                sleep(0.1)
            else:
                self.obj_arduino.cmd_digital_out(1,outPin2,1)
                sleep(0.1)

            #pin 11=Q2=D1=MSB
            if D2=='0':
                self.obj_arduino.cmd_digital_out(1,outPin3,0)
                sleep(0.1)
            else:
                self.obj_arduino.cmd_digital_out(1,outPin3,1)
                sleep(0.1)

            #reads the state of clock
            pinstate=self.obj_arduino.cmd_digital_in(1,clockPin) 

            #clock is common for all FFs
            #thus only 1 if statement for detecting positive edge of clock

            if pinstate!=lastpinstate:
                if pinstate=='1':

                    #order of FFs: serial input-FF2-FF1-FF0

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
    sipo=SIPO(115200)

if __name__=='__main__':
    main()
  
