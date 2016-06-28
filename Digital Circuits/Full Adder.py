import os
import sys
cwd=os.getcwd()
(setpath,Codes)=os.path.split(cwd)
print setpath
sys.path.append(setpath) 

from Arduino.Arduino import Arduino
from time import sleep

class ADDER:

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
        
        self.sumPin=9 #Sum
        self.coutPin=10 #Carry out
        
        self.aPin=5 #input A
        self.bPin=6 #input B
        self.cPin=3 #input Cin (Caryy in)
        
        for _ in range(0,100):
             vala=self.obj_arduino.cmd_digital_in(1,self.aPin)
             print "A= "+vala
             
             valb=self.obj_arduino.cmd_digital_in(1,self.bPin)
             print "B= "+valb

             valc=self.obj_arduino.cmd_digital_in(1,self.cPin)
             print "Cin= "+valc

             #As acoording to the logic circuit of full adder

             #to get Pi: A XOR B
             if vala=='0' and valb=='0':
                 P='0'
             elif vala=='1' and valb=='1':
                 P='0'
             else:
                 P='1'

             #to get Gi: A AND B
             if vala=='1' and valb=='1':
                 G='1'
             else:
                 G='0'

             #to get Sum: Pi XOR Cin
             if P=='0' and valc=='0':
                 self.obj_arduino.cmd_digital_out(1,self.sumPin,0)
                 sleep(0.1)
             elif P=='1' and valc=='1':
                 self.obj_arduino.cmd_digital_out(1,self.sumPin,0)
                 sleep(0.1)
             else:
                 self.obj_arduino.cmd_digital_out(1,self.sumPin,1)
                 sleep(0.1)

             #To get Carry out

             #Pi AND Cin
             if P=='1' and valc=='1':
                 temp='1'
             else:
                 temp='0'

             # Gi OR temp
             if G=='0' and temp=='0':
                 self.obj_arduino.cmd_digital_out(1,self.coutPin,0)
                 sleep(0.1)
             else:
                 self.obj_arduino.cmd_digital_out(1,self.coutPin,1)
                 sleep(0.1)

       


    def exit(self):
        self.obj_arduino.close_serial()

def main():
    obj_adder=ADDER(115200)

if __name__=='__main__':
    main()

        
