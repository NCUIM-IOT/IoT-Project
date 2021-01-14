
import time 
import sys
from adafruit_servokit import ServoKit 


nbPCAServo=1


MIN_IMP  =[500]
MAX_IMP  =[2500]
MIN_ANG  =[0]
MAX_ANG  =[180]


pca = ServoKit(channels=16)

def init():

    for i in range(nbPCAServo):
        pca.servo[i].set_pulse_width_range(MIN_IMP[i] , MAX_IMP[i])



def main():

    global first
    first=input('input the test angle')
    pcaFirstScenario();

    
def pcaFirstScenario():

    for j in range(MIN_ANG[0],int(first),1):
        print("Send angle {} to Servo".format(j))
        pca.servo[0].angle = j
    for j in range(int(first),MIN_ANG[0],-1):
        print("Send angle {} to Servo".format(j))
        pca.servo[0].angle = j
        time.sleep(0.01)
    pca.servo[0].angle=None #disable channel
    time.sleep(0.5)
    sys.exit()


if __name__ == '__main__':
    init()
    main()
