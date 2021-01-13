
from adafruit_servokit import ServoKit 
import time
import sys


#Constants
nbPCAServo=6

#Parameters
MIN_IMP  =[500, 500, 500, 500, 500, 500]
MAX_IMP  =[2500, 2500, 2500, 2500, 2500, 2500]
INT_ANG  =[179, 0, 70, 0, 110, 90]
MIN_ANG  =[179, 0, 45, 0, 60, 0]
MAX_ANG  =[180, 180, 180, 0, 150, 180]

#Objects
pca = ServoKit(channels=16)

for i in range(nbPCAServo):
    pca.servo[i].set_pulse_width_range(MIN_IMP[i] , MAX_IMP[i])
    pca.servo[i].angle = INT_ANG[i]
    j=INT_ANG[i]
    print("Send angle {} to Servo{}".format(j,i))
    
sys.exit()