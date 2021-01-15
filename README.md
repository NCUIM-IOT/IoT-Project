# IoT-Project - Bacne Helper

## Introduction

It's an IoT project that can help people put medicine on their bacnes. By using the recognition and the robotic arm, the device can complete the whole process. And the user can watch the streaming by the user interface.

## Hardware Components

1. Raspberry Pi 3 *1
2. MG996R Servo Motor *6
3. 6-DOF Robotic Arm *1
4. Pi Camera *1
5. PCA9685 (I2C Interface) *1
6. Switching Power Supply *1 (with wires)
7. Dupont Lines *4 (at least)

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

### MG996R Servo Motor

Before you put them onto the robotic arm, you can first test the way they operate by the code. It will first ask you enter a number between 0-180, and you will see the motor operating.
You can also use it to test a single motor after your arm is ready. I will explain it later.
The code is in "IoT_Project/servo_test.py")

### Switched Power Supply

It can provide the power that the motors need by transfer the AC to DC.
Because it connect to the socket directly so <font color="red"> please be careful</font>


![image](https://raw.githubusercontent.com/oohyuti/IoT-Project/main/Power%20Supply.JPG)

Tip : I stick the chopsticks on the wire and hold the chopsticks instead of the plug itself. So that if there is anything wrong, you won't get hurt.
![image](https://raw.githubusercontent.com/oohyuti/IoT-Project/main/plug.jpg)

### 6-DOF Robotic Arm

If you got the arm and the servo motors seperately, you can puzzle them up by [this link](https://www.taiwansensor.com.tw/6軸機械手臂組裝教學/).(Remember to double check the direction or you may need to reinstall them if you put them in the wrong directtion.

### Custom Vision

It is a service provided by Microsoft. You can use it to train your acne model and use the prediction key to call the API in your code. The thing you need to do is to look for all kinds of acne's picture and tag those acnes in the custom vision page.(https://blog.cavedu.com/2019/09/30/azure-custom-vision/).

## Connect the components - How it looks like

### STEP 1 : Put the pi camera on your raspberry pi 3

### STEP 2 : Connect the PCA9685 and your raspberry pi 3

You can check out the picture and you can put the 'vcc' to pinout 1(3v3 power), too.
<font color="red"> Please be careful! Don't insert the wrong pinout or it will easily burn out. </font>

![image](https://www.aranacorp.com/wp-content/uploads/16-channel-pwm-controller-pca9685-raspberry-pi_bb-1080x675.png)


### STEP 3 : Connect the servo motors and your PCA9685

There are sixteen positions that can provide the control of the servo motors. So you can insert the dupont lines one by one from the 0 position.

### STEP 4 : Connect the PCA9685 and the power supply

<font color="red"> Please be careful when you plug into the socket and don't touch the power supply when it's powered. </font>
![image](https://raw.githubusercontent.com/oohyuti/IoT-Project/main/PCA9685_Power%20Supply.jpg)

### You can watch the video to check if you have connected all the things right.
[![](http://img.youtube.com/vi/Q-PQdTYBZAw/0.jpg)](http://www.youtube.com/watch?v=Q-PQdTYBZAw "")

## Test the robotic arm

After connecting all the hardware components. You can now 

## Reference Link

1. servo_test.py & init_servo_test.py : https://www.aranacorp.com/en/using-a-pca9685-module-with-raspberry-pi/
2. connect the PCA9685 and your raspberry pi 3 : https://www.aranacorp.com/wp-content/uploads/16-channel-pwm-controller-pca9685-raspberry-pi_bb-1080x675.png
