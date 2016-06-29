import os
import sys
cwd=os.getcwd()
(setpath,Codes)=os.path.split(cwd)
print setpath
sys.path.append(setpath) 

from Arduino.Arduino import Arduino
from time import sleep

class MUX:

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
        
        self.ledPin=9 #Output

        #select lines        
        self.aPin=6 #input A (MSB)
        self.bPin=7 #input B (LSB)

        #inputs
        self.Pin4=5 #input 4 (MSB)
        self.Pin3=4 #input 3
        self.Pin2=3 #input 2
        self.Pin1=2 #input 1 (LSB)
        
        
        for _ in range(0,200):
             i4=self.obj_arduino.cmd_digital_in(1,self.Pin4) #MSB input
             i3=self.obj_arduino.cmd_digital_in(1,self.Pin3)
             i2=self.obj_arduino.cmd_digital_in(1,self.Pin2)
             i1=self.obj_arduino.cmd_digital_in(1,self.Pin1) #LSB input

             A=self.obj_arduino.cmd_digital_in(1,self.aPin) #MSB select line input
             B=self.obj_arduino.cmd_digital_in(1,self.bPin) #LSB select line input
                    
             
             if A=='0' and B=='0':
                 #input i1 is selected, output is same as i1
                 if i1=='0':
                     self.obj_arduino.cmd_digital_out(1,self.ledPin,0)
                     sleep(0.1)
                 else:
                     self.obj_arduino.cmd_digital_out(1,self.ledPin,1)
                     sleep(0.1)

             elif A=='0' and B=='1':
                 #input i2 is selected, output is same as i2
                 if i2=='0':
                     self.obj_arduino.cmd_digital_out(1,self.ledPin,0)
                     sleep(0.1)
                 else:
                     self.obj_arduino.cmd_digital_out(1,self.ledPin,1)
                     sleep(0.1)

             elif A=='1' and B=='0':
                 #input i3 is selected, output is same as i3
                 if i3=='0':
                     self.obj_arduino.cmd_digital_out(1,self.ledPin,0)
                     sleep(0.1)
                 else:
                     self.obj_arduino.cmd_digital_out(1,self.ledPin,1)
                     sleep(0.1)

             elif A=='1' and B=='1':
                 #input i4 is selected, output is same as i4
                 if i4=='0':
                     self.obj_arduino.cmd_digital_out(1,self.ledPin,0)
                     sleep(0.1)
                 else:
                     self.obj_arduino.cmd_digital_out(1,self.ledPin,1)
                     sleep(0.1)

             else:
                 print ("Invalid input!")

       


    def exit(self):
        self.obj_arduino.close_serial()

def main():
    obj_mux=MUX(115200)

if __name__=='__main__':
    main()

        
