
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

class PISO:

    
    
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

        sl='0' #shift/!load

        D2='0' #MSB input
        D1='0' #middle bit input=MSB output
        D0='0' #LSB input=middle bit output
        Q='0' #LSB output

        #Parallel inputs
        inPin1=5 #LSB input
        inPin2=6 #middle bit 
        inPin3=7 #MSB 

        #Serial output
        outPin=9 #LSB = Q
         

        #external clock pulse
        clockPin=2

        #Shift/!Load input
        slPin=3
        


        for _ in range(0,500):

            #pin 9=Q=LSB output
            if D0=='0':
                self.obj_arduino.cmd_digital_out(1,outPin,0)
                sleep(0.1)
            else:
                self.obj_arduino.cmd_digital_out(1,outPin,1)
                sleep(0.1)

            #reads the state of Shift/!Load
            sl=self.obj_arduino.cmd_digital_in(1,slPin)

            #reads the state of clock
            pinstate=self.obj_arduino.cmd_digital_in(1,clockPin) 

            #clock is common for all FFs
            #thus only 1 if statement for detecting positive edge of clock

            if pinstate!=lastpinstate:
                if pinstate=='1':

                    #order of FFs: serial input-FF2-FF1-FF0

                    if sl=='0': #parallel load mode
                        D0=self.obj_arduino.cmd_digital_in(1,inPin1)
                        D1=self.obj_arduino.cmd_digital_in(1,inPin2)
                        D2=self.obj_arduino.cmd_digital_in(1,inPin3)

                    else: #sl==1 i.e. serial shift mode

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
                        D2='0'

                    
                sleep(0.05)
            lastpinstate=pinstate
                    
                    
            



    def exit(self):
        self.obj_arduino.close_serial()

def main():
    piso=PISO(115200)

if __name__=='__main__':
    main()
  
