
import os
import sys
cwd=os.getcwd()
(setpath_,Trials)=os.path.split(cwd)
print setpath_
(setpath,Codes)=os.path.split(setpath_)
print setpath
sys.path.append(setpath) 

from Arduino.Arduino import Arduino
from Arduino.IC_methods import IC_methods
from time import sleep

class Try:

    
    
    def __init__(self,baudrate):
        self.baudrate=baudrate
        self.setup()
        self.run()
        self.exit()


    def setup(self):
        global obj_arduino
        obj_arduino=Arduino()
        self.port=obj_arduino.locateport()
        obj_arduino.open_serial(1,self.port,self.baudrate)

        self.obj_icm=IC_methods(self.baudrate)

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
            if Q=='0':
                obj_arduino.cmd_digital_out(1,outPin,0)
                sleep(0.1)
            else:
                obj_arduino.cmd_digital_out(1,outPin,1)
                sleep(0.1)

            #reads the state of Shift/!Load
            sl=obj_arduino.cmd_digital_in(1,slPin)

            #reads the state of clock
            pinstate=obj_arduino.cmd_digital_in(1,clockPin) 

            #clock is common for all FFs
            #thus only 1 if statement for detecting positive edge of clock

            if pinstate!=lastpinstate:
                if pinstate=='1':

                    #order of FFs: serial input-FF2-FF1-FF0

                    if sl=='0':
                        D0=obj_arduino.cmd_digital_in(1,inPin1)
                        D1=obj_arduino.cmd_digital_in(1,inPin2)
                        D2=obj_arduino.cmd_digital_in(1,inPin3)

                    else:

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
                    
            self.obj_icm.cmd_shift_in(1,2,3,4)  
            



    def exit(self):
        obj_arduino.close_serial()

def main():
    piso=Try(115200)

if __name__=='__main__':
    main()
  
