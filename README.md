# IoT-Project - Bacne Helper

## Introduction

It's an IoT project that can help people put medicine on their bacnes. By using the recognition and the robotic arm, the device can complete the whole process. And the user can watch the streaming by the user interface.


## System Structure

## Hardware Components

- Raspberry Pi 3 *1
- MG996R Servo Motor *6
- 6-DOF Robotic Arm *1
- Pi Camera *1
- PCA9685 (I2C Interface) *1
- Switching Power Supply *1
- Dupont Lines *4 (at least)

## Preparation

#### Raspberry Pi 3 

You need to install some packages to start this project.
`
pip3 install flask
`
`
pip3 install opencv-python
`
`
pip3 install adafruit-circuitpython-servokit
`

#### MG996R Servo Motor *6

Before you put them onto the robotic arm, you can first test the way they operate by the code. It will first ask you enter a number between 0-180, and you will see the motor operating.
You can also use it to test a single motor after your arm is ready. I will explain it later.
The code is in "IoT_Project/servo_test.py")

- 6-DOF Robotic Arm *1

If you got the arm and the servo motors seperately, you can puzzle them up by [this link](https://www.taiwansensor.com.tw/6軸機械手臂組裝教學/).(Remember to double check the direction or you may need to reinstall them if you put them in the wrong directtion.

- (Custom Vision)[https://www.customvision.ai]

It is a service provided by Microsoft. You can use it to train your acne model and use the prediction key to call the API in your code. The thing you need to do is to look for all kinds of acne's picture and tag those acnes in the custom vision page. You can see the process in (this link)[https://blog.cavedu.com/2019/09/30/azure-custom-vision/].


## Testing the robotic arm

## Reference Link

- https://www.aranacorp.com/en/using-a-pca9685-module-with-raspberry-pi/
