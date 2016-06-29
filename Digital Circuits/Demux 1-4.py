import os
import sys
cwd=os.getcwd()
(setpath,Codes)=os.path.split(cwd)
print setpath
sys.path.append(setpath) 

from Arduino.Arduino import Arduino
from time import sleep

class DEMUX:

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
        
        self.inPin=5 #Input

        #select lines        
        self.aPin=6 #input A (MSB)
        self.bPin=7 #input B (LSB)

        #outputs
        self.ledPin4=11 #output 4 (MSB)
        self.ledPin3=10 #output 3
        self.ledPin2=9 #output 2
        self.ledPin1=8 #output 1 (LSB)
        
        
        for _ in range(0,500):
             i=self.obj_arduino.cmd_digital_in(1,self.inPin) #input
             

             A=self.obj_arduino.cmd_digital_in(1,self.aPin) #MSB select line input
             B=self.obj_arduino.cmd_digital_in(1,self.bPin) #LSB select line input

             print ("A= "+A+", B= "+B+", i= "+i)
            
                    
             if i=='0': #all outputs will be zero irrespective of which one is selected
                 self.obj_arduino.cmd_digital_out(1,self.ledPin1,0)
                 self.obj_arduino.cmd_digital_out(1,self.ledPin2,0)
                 self.obj_arduino.cmd_digital_out(1,self.ledPin3,0)
                 self.obj_arduino.cmd_digital_out(1,self.ledPin4,0)
                 sleep(0.1)
                     

             elif i=='1': 
                 if A=='0' and B=='0': #input i is seen at first output pin (LSB)
                     self.obj_arduino.cmd_digital_out(1,self.ledPin1,1)
                     self.obj_arduino.cmd_digital_out(1,self.ledPin2,0)
                     self.obj_arduino.cmd_digital_out(1,self.ledPin3,0)
                     self.obj_arduino.cmd_digital_out(1,self.ledPin4,0)
                     sleep(0.1)
                     
                 elif A=='0' and B=='1': #input i is seen at second output pin
                     self.obj_arduino.cmd_digital_out(1,self.ledPin2,1)
                     self.obj_arduino.cmd_digital_out(1,self.ledPin1,0)
                     self.obj_arduino.cmd_digital_out(1,self.ledPin3,0)
                     self.obj_arduino.cmd_digital_out(1,self.ledPin4,0)
                     sleep(0.1)
                     
                 elif A=='1' and B=='0': #input i is seen at third output pin
                     self.obj_arduino.cmd_digital_out(1,self.ledPin3,1)
                     self.obj_arduino.cmd_digital_out(1,self.ledPin1,0)
                     self.obj_arduino.cmd_digital_out(1,self.ledPin2,0)
                     self.obj_arduino.cmd_digital_out(1,self.ledPin4,0)
                     sleep(0.1)
                     
                 elif A=='1' and B=='1': #input i is seen at fourth output pin (MSB)
                     self.obj_arduino.cmd_digital_out(1,self.ledPin4,1)
                     self.obj_arduino.cmd_digital_out(1,self.ledPin1,0)
                     self.obj_arduino.cmd_digital_out(1,self.ledPin2,0)
                     self.obj_arduino.cmd_digital_out(1,self.ledPin3,0)
                     sleep(0.1)

                 

    def exit(self):
        self.obj_arduino.close_serial()

def main():
    obj_demux=DEMUX(115200)

if __name__=='__main__':
    main()
