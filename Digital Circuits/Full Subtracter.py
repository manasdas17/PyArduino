import os
import sys
cwd=os.getcwd()
(setpath,Codes)=os.path.split(cwd)
print setpath
sys.path.append(setpath) 

from Arduino.Arduino import Arduino
from time import sleep

class SUBTRACTER:

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
        
        self.diffPin=9 #Difference
        self.boutPin=10 #Borrow out
        
        self.aPin=5 #input A
        self.bPin=6 #input B
        self.binPin=3 #input Bin (Borrow in)
        
        for _ in range(0,100):
             vala=self.obj_arduino.cmd_digital_in(1,self.aPin)
             print "A= "+vala
             
             valb=self.obj_arduino.cmd_digital_in(1,self.bPin)
             print "B= "+valb

             valbin=self.obj_arduino.cmd_digital_in(1,self.binPin)
             print "Bin= "+valbin

             #As acoording to the logic circuit of full subtracter

             #First half subtracter

             #Difference
             #A XOR B
             if vala=='0' and valb=='0':
                 fsdiff='0'
             elif vala=='1' and valb=='1':
                 fsdiff='0'
             else:
                 fsdiff='1'

             #borrow out
             #A NOT
             if vala=='1':
                 fsnot='0'
             else:
                 fsnot='1'

             #B AND fsnot
             if valb=='1' and fsnot=='1':
                 fsb='1'
             else:
                 fsb='0'

             #second half subtacter

             #difference
             #fsdiff XOR Bin
             if fsdiff=='0' and valbin=='0':
                 self.obj_arduino.cmd_digital_out(1,self.diffPin,0)
                 sleep(0.1)
             elif fsdiff=='1' and valbin=='1':
                 self.obj_arduino.cmd_digital_out(1,self.diffPin,0)
                 sleep(0.1)
             else:
                 self.obj_arduino.cmd_digital_out(1,self.diffPin,1)
                 sleep(0.1)

             #borrow out
             #fsdiff NOT
             if fsdiff=='1':
                 ssnot='0'
             else:
                 ssnot='1'

             #Bin and ssnot
             if valbin=='1' and ssnot=='1':
                 ssand='1'
             else:
                 ssand='0'

             #ssand OR fsb
             if ssand=='0' and fsb=='0':
                 self.obj_arduino.cmd_digital_out(1,self.boutPin,0)
                 sleep(0.1)
             else:
                 self.obj_arduino.cmd_digital_out(1,self.boutPin,1)
                 sleep(0.1)
       


    def exit(self):
        self.obj_arduino.close_serial()

def main():
    obj_subtracter=SUBTRACTER(115200)

if __name__=='__main__':
    main()

        
