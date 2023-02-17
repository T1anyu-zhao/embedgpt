# Embedded System Coursework of group EmbedGPT

## myPI Face ID Access Control System
The key aspect of this project is to develop on a Raspberry Pi to implement a Face ID system for unlocking doors in schools and companies. It can replace the ID cards, which are always forgotten or stolen from the owner. It is based on OpenCV, which is powerful at real-time computer vision and free to use.

## Devices Used
Raspberry Pi Zero W          x1
OV5647 Mini Camera Module    x1
Red LED & Green LED 
Resistors

## Install
Here are the libraries need to be install for the project:
sudo pip3 install opencv_python 
sudo pip3 install opencv-contrib-python
sudo apt-get install libatlas-base-dev
sudo apt-get install libjasper-dev 
sudo apt-get install libqtgui4 
sudo apt-get install libqt4-test


## Raspi app for face recognition 
The premise of facial recognition is to identify the resence of a face in the image or video frame which is done with Haar Cascade Algorithm. 
The code for recognising faces can be devided into three parts, data gathering, train the recognizer and recognition.

Object Detection using Haar feature-based cascade classifiers is an effective object detection method. It is a machine learning based approach where a cascade function is trained from a lot of positive and negative images. It is then used to detect objects in other images.

OpenCV already contains many pre-trained classifiers for face, eyes, smile, etc. Those XML files can be download from haarcascades directory.


## Vue website application
The Web application can communication with the Raspberry Pi board by http protocol. The board will transmit the message that contains the time, ID and image of visitors. The information will be used for recording in database and representing on the web page. 

## Server and Database
This project is an Express server that is designed to process visitor records. The server has been built using Node.js and Express, and it allows users to record visitor information and store it in a database for future reference.

The server has been designed to be fast and efficient, and it can handle a large number of visitors at any given time. The data is stored in a MongoDB database, which makes it easy to manage and retrieve data as needed. The server also includes several API endpoints that allow users to retrieve data from the database and perform various operations on the visitor records. With its easy-to-use API and efficient design, it is the ideal solution for businesses and organizations that need to keep track of their visitors and their data.

## Flask local control application
This web application utilizes Flask, a Python web framework, to stream video from a camera and process data in real-time. The app allows users to access a live video feed from a camera and analyze data collected from the camera's stream. The application has a user-friendly interface with multiple features, including the ability to capture images from the video stream and process data.

## Contributor
dx320      Obivating  

kl2420     KaiwenLiu1227  

az2120     T1anyu-zhao  

## Reference 
The project is refer to the tutorial :https://www.hackster.io/mjrobot/real-time-face-recognition-an-end-to-end-project-a10826
