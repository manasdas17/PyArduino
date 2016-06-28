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

class JK_FF_edge:

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

        self.S='0'
        self.R='1'

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

        self.pinstate='0'
        self.lastpinstate='0'


        for _ in range(0,500):

            if self.Q=='0':
                self.obj_arduino.cmd_digital_out(1,self.qPin,0) #Gives low output at Q
                self.obj_arduino.cmd_digital_out(1,self.qbarPin,1) #Gives high output at Qbar
                sleep(0.1)
            else:
                self.obj_arduino.cmd_digital_out(1,self.qPin,1) #Gives high output at Q
                self.obj_arduino.cmd_digital_out(1,self.qbarPin,0) #Gives low output at Qbar
                sleep(0.1)


            self.pre=self.obj_arduino.cmd_digital_in(1,self.prePin) #Reads preset input
            self.clr=self.obj_arduino.cmd_digital_in(1,self.clrPin) #Reads clear input

            if self.pre=='0' and self.clr=='1':
                self.S='1'
                self.R='0'
                self.Q='1'
                
            elif self.pre=='1' and self.clr=='0':
                self.S='0'
                self.R='1'
                self.Q='0'

            #Normal functioning when both are HIGH
            elif self.pre=='1' and self.clr=='1':
                
                self.pinstate=self.obj_arduino.cmd_digital_in(1,self.clockPin) #Reads clock input

                if self.pinstate!=self.lastpinstate: #edge detection
                    if self.pinstate=='1': #Positive edge

                        #MASTER
                        #JK FF Code
                        self.J=self.obj_arduino.cmd_digital_in(1,self.jPin)
                        self.K=self.obj_arduino.cmd_digital_in(1,self.kPin)

                        if self.J=='0' and self.K=='1':
                            self.S='0'
                            self.R='1'
                        elif self.J=='1' and self.K=='0':
                            self.S='1'
                            self.R='0'
                        elif self.J=='1' and self.K=='1':
                            temp=self.S
                            self.S=self.R
                            self.R=temp
                        else:
                            pass
                    else:
                        pass

                    if self.pinstate=='0':

                        #SLAVE
                        #JK FF code only for state 01 and 10
                        if self.S=='0' and self.R=='1':
                            self.Q='0'
                        elif self.S=='1' and self.R=='0':
                            self.Q='1'
                        else:
                            pass
                    else:
                        pass

                    sleep(0.05)
                self.lastpinstate=self.pinstate
            else:
                pass
    


    def exit(self):
        self.obj_arduino.close_serial()

def main():
    obj_jkffe=JK_FF_edge(115200)

if __name__=='__main__':
    main()
  
