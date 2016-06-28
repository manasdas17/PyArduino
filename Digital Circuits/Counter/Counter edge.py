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

class COUNTER:

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

        self.pinstate0='0' #input, clock pulse to FF1
        self.lastpinstate0='0'

        self.pinstate1='0' #output of FF1 (LSB), clock pulse to FF2
        self.lastpinstate1='0'

        self.pinstate2='0' #output of FF2 (middle bit)), clock pulse to FF3
        self.lastpinstate2='0'

        self.pinstate3='0' #output of FF3 (MSB)
        self.lastpinstate3='0'

        #outputs
        self.Pin1=9 #LSB
        self.Pin2=10 #middle bit
        self.Pin3=11 #MSB

        #external clock
        self.clockPin=5
        


        for _ in range(0,500):
            
            #LSB
            if self.pinstate1=='0':
                self.obj_arduino.cmd_digital_out(1,self.Pin1,0)
                sleep(0.1)
            else:
                self.obj_arduino.cmd_digital_out(1,self.Pin1,1)
                sleep(0.1)

            #middle bit
            if self.pinstate2=='0':
                self.obj_arduino.cmd_digital_out(1,self.Pin2,0)
                sleep(0.1)
            else:
                self.obj_arduino.cmd_digital_out(1,self.Pin2,1)
                sleep(0.1)

            #MSB
            if self.pinstate3=='0':
                self.obj_arduino.cmd_digital_out(1,self.Pin3,0)
                sleep(0.1)
            else:
                self.obj_arduino.cmd_digital_out(1,self.Pin3,1)
                sleep(0.1)


            self.pinstate0=self.obj_arduino.cmd_digital_in(1,self.clockPin)

            #negative edge of clock pulse to FF1
            if self.pinstate0!=self.lastpinstate0:
                if self.pinstate0=='0':
                    #toggle i.e if output is 0, change it to 1
                    if self.pinstate1=='0':
                        self.pinstate1='1'
                    else:
                        self.pinstate1='0'
                else:
                    pass
                sleep(0.05)
            self.lastpinstate0=self.pinstate0

            #negative edge of clock pulse to FF2
            if self.pinstate1!=self.lastpinstate1:
                if self.pinstate1=='0':
                    #toggle i.e if output is 0, change it to 1
                    if self.pinstate2=='0':
                        self.pinstate2='1'
                    else:
                        self.pinstate2='0'
                else:
                    pass
                sleep(0.05)
            self.lastpinstate1=self.pinstate1

            #negative edge of clock pulse to FF1
            if self.pinstate2!=self.lastpinstate2:
                if self.pinstate2=='0':
                    #toggle i.e if output is 0, change it to 1
                    if self.pinstate3=='0':
                        self.pinstate3='1'
                    else:
                        self.pinstate3='0'
                else:
                    pass
                sleep(0.05)
            self.lastpinstate2=self.pinstate2

 



    def exit(self):
        self.obj_arduino.close_serial()

def main():
    obj_count=COUNTER(115200)

if __name__=='__main__':
    main()
  
