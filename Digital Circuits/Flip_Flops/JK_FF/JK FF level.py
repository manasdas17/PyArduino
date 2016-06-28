import os
import sys
cwd=os.getcwd()
(setpath__,JK_FF)=os.path.split(cwd)
print setpath__
(setpath_,Flip_Flops)=os.path.split(setpath__)
print setpath_
(setpath,Codes)=os.path.split(setpath_)
print setpath
sys.path.append(setpath) 

from Arduino.Arduino import Arduino
from time import sleep

class JK_FF:

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

        self.J='0'
        self.K='0'

        self.jPin=5
        self.kPin=6

        self.prePin=3
        self.clrPin=4

        #assuming initial state:
        self.Q='0'
        self.Qbar='1'

        self.qPin=9
        self.qbarPin=10

        self.clockPin=2 #external clock


        for _ in range(0,500):

            if self.Q=='0':
                self.obj_arduino.cmd_digital_out(1,self.qPin,0) #Gives low output at Q
                sleep(0.05)
            elif self.Q=='1':
                self.obj_arduino.cmd_digital_out(1,self.qPin,1) #Gives high output at Q
                sleep(0.05)
            else:
                pass
               
            if self.Qbar=='0':
                self.obj_arduino.cmd_digital_out(1,self.qbarPin,0) #Gives low output at Qbar
                sleep(0.05)
            elif self.Qbar=='1':
                self.obj_arduino.cmd_digital_out(1,self.qbarPin,1) #Gives high output at Qbar
                sleep(0.05)
            else:
                pass

            self.J=self.obj_arduino.cmd_digital_in(1,self.jPin) #Reads the input J
            self.K=self.obj_arduino.cmd_digital_in(1,self.kPin) #Reads the input K

            self.pre=self.obj_arduino.cmd_digital_in(1,self.prePin) #Reads the input Preset
            self.clr=self.obj_arduino.cmd_digital_in(1,self.clrPin) #Reads the input Clear

            if self.pre=='0' and self.clr=='1':
                self.Q='1'
                self.Qbar='0'

            elif self.pre=='1' and self.clr=='0':
                self.Q='0'
                self.Qbar='1'

            #Preset and clear are active low inputs, thus normal functioning of flip flop happens when both are HIGH
            elif self.pre=='1' and self.clr=='1':
                if self.obj_arduino.cmd_digital_in(1,self.clockPin)=='1':

                    if self.J=='0' and self.K=='1':
                        self.Q='0'
                        self.Qbar='1'
                    elif self.J=='1' and self.K=='0':
                        self.Q='1'
                        self.Qbar='0'
                    elif self.J=='1' and self.K=='1': #toggle state
                        temp=self.Q
                        self.Q=self.Qbar
                        self.Qbar=temp
                    else:
                        pass
                







    def exit(self):
        self.obj_arduino.close_serial()

def main():
    obj_jkff=JK_FF(115200)

if __name__=='__main__':
    main()
  
