import os
import sys
cwd=os.getcwd()
(setpath_,Counter)=os.path.split(cwd)
print setpath_
(setpath,Codes)=os.path.split(setpath_)
print setpath
sys.path.append(setpath) 

from Arduino.Arduino import Arduino
from time import sleep

class COUNTER_wo_ff:
    
    
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

        #outputs
        Pin1=9 #LSB
        Pin2=10 #middle bit
        Pin3=11 #MSB

        i=0
        a=0
        b=0
        c=0


        for _ in range(0,500):
            
            pinstate=self.obj_arduino.cmd_digital_in(1,clockPin)

            #negative edge of clock pulse to FF1
            if pinstate!=lastpinstate:
                if pinstate=='0':
                    i+=1
                else:
                    pass
                sleep(0.05)
            else:
                pass
            lastpinstate=pinstate

            a=i%2
            b=(i/2)%2
            c=(i/4)%2

            self.obj_arduino.cmd_digital_out(1,Pin1,a) #LSB
            self.obj_arduino.cmd_digital_out(1,Pin2,b) #middle bit
            self.obj_arduino.cmd_digital_out(1,Pin3,c) #MSB
            sleep(0.1)

            if i>7:
                i=0
            else:
                pass



    def exit(self):
        self.obj_arduino.close_serial()

def main():
    obj_count_wo_ff=COUNTER_wo_ff(115200)

if __name__=='__main__':
    main()
  
