from flask import Flask
from flask import render_template
from flask import request
from flask import Response
from flask import url_for
from adafruit_servokit import ServoKit 
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials
import time    #https://docs.python.org/fr/3/library/time.htmlimport picamera
import cv2
import socket 
import io
import math


app=Flask(__name__)


credentials = ApiKeyCredentials(in_headers={"Prediction-key": "<Your Prediction Key>"})
predictor = CustomVisionPredictionClient("<Your Endpoint>", credentials)


#Constants
nbPCAServo=6

#Parameters
MIN_IMP  =[500, 500, 500, 500, 500, 500]
MAX_IMP  =[2500, 2500, 2500, 2500, 2500, 2500]
INT_ANG  =[179, 30, 70, 0, 110, 0]
MIN_ANG  =[179, 0, 45, 0, 60, 0]
MAX_ANG  =[180, 180, 180, 50, 150, 180]

#Objects
pca = ServoKit(channels=16)


def init():
    for i in range(nbPCAServo):
        pca.servo[i].set_pulse_width_range(MIN_IMP[i] , MAX_IMP[i])
        pca.servo[i].angle = INT_ANG[i]
        j=INT_ANG[i]
        print("Send angle {} to Servo{}".format(j,i))
            
def move(i,x):
    for j in range(INT_ANG[i],x,1):
        pca.servo[i].angle = j
        time.sleep(0.03)
        
def back(i,x):
    for j in range(x,INT_ANG[i],-1):
        pca.servo[i].angle = j
        time.sleep(0.03)
    


def calculateX(x):
    if x<400:
        x=400-x
    else:
        x=x-400
    
    x=x/20
    degree=int(math.degrees(math.atan(x/10)))

    if x<20:
        degree=90+degree
    else:
        degree=90-degree
        
    return degree

@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        return render_template('index.html')
    else: 
        return render_template('index.html')

def gen(): 
    """Video streaming generator function."""
    vc = cv2.VideoCapture(-1)
    vc.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
    vc.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)
    
    while True:
        rval, frame = vc.read() 
        cv2.imwrite('capture.jpg', frame)
        global results
        with open("capture.jpg", mode="rb") as captured_image:
            results = predictor.detect_image("<Your Project ID>", "<Iteration Name>", captured_image)
        for prediction in results.predictions:
            if prediction.probability > 0.7:
                global bbox
                print(prediction.probability)
                bbox = prediction.bounding_box
                result_image = cv2.rectangle(frame, (int(bbox.left * 800), int(bbox.top * 600)), (int((bbox.left + bbox.width) * 600), int((bbox.top + bbox.height) * 600)), (0, 255, 0), 3)
                cv2.putText(result_image,"Acne",(int(bbox.left*800), int(bbox.top*600)-10),cv2.FONT_HERSHEY_SIMPLEX,0.9,(0,255,0),2)
                cv2.imwrite('result.jpg', result_image)
                yield (b'--frame\r\n' 
                    b'Content-Type: image/jpeg\r\n\r\n' + open('result.jpg', 'rb').read() + b'\r\n')

                
            else:
                yield (b'--frame\r\n' 
                    b'Content-Type: image/jpeg\r\n\r\n' + open('capture.jpg', 'rb').read() + b'\r\n')

        
@app.route('/video_feed') 
def video_feed(): 
    """Video streaming route. Put this in the src attribute of an img tag.""" 
    return Response(gen(),mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/start')
def start():
    init()
    x1 = int(bbox.left * 800)
    x2 = int((bbox.left + bbox.width) * 800)
    y1 = int((bbox.top + bbox.height) * 600)
    y2 = int(bbox.top * 600)
    x=(x1+x2)/2
    y=(y1+y2)/2
    
    degreeX=calculateX(x)
    degreeY=80
    degreeZ=90
    degree=50
    print("degreeX={}".format(degreeX))
    move(5,degreeX)
    move(4,degreeZ)
    move(2,degreeY)
    move(3,30)
    time.sleep(3)
    
    back(3,30)
    back(2,degreeY)
    back(4,degreeZ)
    back(5,degreeX)
    
    
    return "nothing"




if __name__=='__main__':
    app.run(debug=True, threaded=True)
    

