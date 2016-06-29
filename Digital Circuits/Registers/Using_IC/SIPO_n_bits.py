import os
import sys
cwd=os.getcwd()
(setpath__,Using_IC)=os.path.split(cwd)
print setpath__
(setpath_,Using_IC)=os.path.split(setpath__)
print setpath_
(setpath,Codes)=os.path.split(setpath_)
print setpath
sys.path.append(setpath) 

from Arduino.Arduino import Arduino

from time import sleep

class SIPO_IC:

    
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
        
        pinstate=0
        n=int(raw_input("Enter no. of bits: "))
        data=[0 for _ in range(0,n)] #an 8-elements list representing an 8 bit binary number
        
        dataPin=11
        clockPin=9
        latchPin=10
        inPin=5

        for _ in range(0,50):
            pinstate=self.obj_arduino.cmd_digital_in(1,inPin)
            if pinstate=='1':
                data[0]=1
                #the msb becomes 1 when input is given
                #high which is henceforth shifted
            else:
                data[0]=0
            print data

            self.obj_arduino.cmd_digital_out(1,latchPin,0)
            self.obj_arduino.cmd_shift_out_n(dataPin,clockPin,'LSBFIRST',data,n)
            self.obj_arduino.cmd_digital_out(1,latchPin,1)
            sleep(0.5)
            for k in range(0,(n-1)):
                data[(n-1)-k]=data[(n-2)-k]
            data[0]=0
            #every element of the matrix is
            #shifted one place to the right
            #so effectively the 8 bit
            #binary number is divided by 2
                  
              

    def exit(self):
        self.obj_arduino.close_serial()

def main():
    sipo=SIPO_IC(115200)

if __name__=='__main__':
    main()
  
