import os
import sys
cwd=os.getcwd()
(setpath,Codes)=os.path.split(cwd)
print setpath
sys.path.append(setpath) 

from Arduino.Arduino import Arduino
from time import sleep

class D2B:

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
        
        #binary Outputs
        self.led1=10 #LSB
        self.led2=11 #middle bit
        self.led3=12 #MSB

        #decimal inputs
        self.Pin1=2 #decimal input 1 (LSB)
        self.Pin2=3 #decimal input 2
        self.Pin3=4 #decimal input 3
        self.Pin4=5 #decimal input 4 
        self.Pin5=6 #decimal input 5
        self.Pin6=7 #decimal input 6
        self.Pin7=8 #decimal input 7 (MSB)
        
        
        for _ in range(0,500):
                       
            d1=self.obj_arduino.cmd_digital_in(1,self.Pin1)
            d2=self.obj_arduino.cmd_digital_in(1,self.Pin2)
            d3=self.obj_arduino.cmd_digital_in(1,self.Pin3)
            d4=self.obj_arduino.cmd_digital_in(1,self.Pin4)
            d5=self.obj_arduino.cmd_digital_in(1,self.Pin5)
            d6=self.obj_arduino.cmd_digital_in(1,self.Pin6)
            d7=self.obj_arduino.cmd_digital_in(1,self.Pin7)

            print (d1+" "+d2+" "+d3+" "+d4+" "+d5+" "+d6+" "+d7)

            #decimal input 0, binary output 000
            if d1=='0' and d2=='0' and d3=='0' and d4=='0' and d5=='0' and d6=='0' and d7=='0':
                self.obj_arduino.cmd_digital_out(1,self.led1,0)
                self.obj_arduino.cmd_digital_out(1,self.led2,0)
                self.obj_arduino.cmd_digital_out(1,self.led3,0)
                sleep(0.1)
                
            #decimal input 1, binary output 001
            elif d1=='1' and d2=='0' and d3=='0' and d4=='0' and d5=='0' and d6=='0' and d7=='0':
                self.obj_arduino.cmd_digital_out(1,self.led1,1)
                self.obj_arduino.cmd_digital_out(1,self.led2,0)
                self.obj_arduino.cmd_digital_out(1,self.led3,0)
                sleep(0.1)
            #decimal input 2, binary output 010
            elif d2=='1' and d3=='0' and d4=='0' and d5=='0' and d6=='0' and d7=='0':
                self.obj_arduino.cmd_digital_out(1,self.led1,0)
                self.obj_arduino.cmd_digital_out(1,self.led2,1)
                self.obj_arduino.cmd_digital_out(1,self.led3,0)
                sleep(0.1)
            #decimal input 3, binary output 011
            elif d3=='1' and d4=='0' and d5=='0' and d6=='0' and d7=='0':
                self.obj_arduino.cmd_digital_out(1,self.led1,1)
                self.obj_arduino.cmd_digital_out(1,self.led2,1)
                self.obj_arduino.cmd_digital_out(1,self.led3,0)
                sleep(0.1)
            #decimal input 4, binary output 100
            elif d4=='1' and d5=='0' and d6=='0' and d7=='0':
                self.obj_arduino.cmd_digital_out(1,self.led1,0)
                self.obj_arduino.cmd_digital_out(1,self.led2,0)
                self.obj_arduino.cmd_digital_out(1,self.led3,1)
                sleep(0.1)
            #decimal input 5, binary output 101
            elif d5=='1' and d6=='0' and d7=='0':
                self.obj_arduino.cmd_digital_out(1,self.led1,1)
                self.obj_arduino.cmd_digital_out(1,self.led2,0)
                self.obj_arduino.cmd_digital_out(1,self.led3,1)
                sleep(0.1)
            #decimal input 6, binary output 110
            elif d6=='1' and d7=='0':
                self.obj_arduino.cmd_digital_out(1,self.led1,0)
                self.obj_arduino.cmd_digital_out(1,self.led2,1)
                self.obj_arduino.cmd_digital_out(1,self.led3,1)
                sleep(0.1)
            #decimal input 7, binary output 111
            elif d7=='1':
                self.obj_arduino.cmd_digital_out(1,self.led1,1)
                self.obj_arduino.cmd_digital_out(1,self.led2,1)
                self.obj_arduino.cmd_digital_out(1,self.led3,1)
                sleep(0.1)
            else:
                self.obj_arduino.cmd_digital_out(1,self.led1,0)
                self.obj_arduino.cmd_digital_out(1,self.led2,0)
                self.obj_arduino.cmd_digital_out(1,self.led3,0)
                sleep(0.1)
             

       


    def exit(self):
        self.obj_arduino.close_serial()

def main():
    obj_d2b=D2B(115200)

if __name__=='__main__':
    main()

        
