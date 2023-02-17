import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)

import time
import smbus2

si7021_ADD = 0x40
si7021_READ_TEMPERATURE = 0xF3

bus = smbus2.SMBus(1)



import cv2
import numpy as np
import os 
import requests
import json
import base64
from datetime import datetime
import time

def visitHTTP(name, image, date):
    base_url = "http://52.1.172.234:3000/api/v1/"
    res = requests.get(base_url + "visitors")
    visit_list = res.json()
    for item in visit_list:
        # existed visitor
        if name == item.get('name'):
            #print(item)
            # get visitor id
            v_id = item.get('_id')
            record_json = {
                "date": date,
                "photo": image,
                "visitor": v_id,
            }
            # print(record_json)
            visitor_json = item
            # if have visit record, update time
            if item.get('lastVisit'):
                item['lastVisit'] = date
            if item.get('image'):
                item['image'] = image
            # create new records
            requests.post(base_url + "visitRecords", data=record_json, headers={})
            # update visitor info
            requests.put(base_url + "visitors/" + v_id, data=visitor_json, headers={})
            # print("verified visitor, " + name + " new record made")
            return
        v_json = {
        "name": name,
        "image": image,
        "lastVisit": date
    }
    # print(v_json)
    # create new visitor
    requests.post(base_url + "visitors", data=v_json, headers={})
    # print("new visitor " + name + " added")
        
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

font = cv2.FONT_HERSHEY_SIMPLEX

#iniciate id counter
id = 0

# names related to ids: example ==> SuperDvD: id=1,  etc
names = ['None', 'SuperDvD','WhiteBirds','Stott'] 

# Initialize and start realtime video capture
cam = cv2.VideoCapture(0)
cam.set(3, 320) # set video widht
cam.set(4, 240) # set video height

# Define min window size to be recognized as a face
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)

nameList = []

while True:
    ret, img =cam.read()
    img = cv2.flip(img, -1) # Flip vertically

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale( 
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW), int(minH)),
       )

    for(x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])

        # Check if confidence is less them 100 ==> "0" is perfect match 
        if (confidence < 100):
            id = names[id]
            confidence = "  {0}%".format(round(130 - confidence))
        else:
            id = "unknown"
            confidence = "  {0}%".format(round(100 - confidence))
        
        cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
        cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)  

    cv2.imshow('image', img)    

    if id == 0 or id == 'unknown':
        print("No new face detected")
        #red led on when unknowm detect
        GPIO.output(16,GPIO.HIGH)
        GPIO.output(18,GPIO.LOW)
        time.sleep(1)
    else:
        if id in nameList:
            print("User " + str(id) + " already exist")
        else:
            nameList.append(id)
            print("New user detect: " + str(id))
            img = cv2.resize(img,(128,128),interpolation=cv2.INTER_CUBIC)
            cv2.imwrite('test.jpg',img,[int(cv2.IMWRITE_JPEG_QUALITY),50])

            with open("test.jpg", "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read())
            date = datetime.now()
            image = "data:image/jpeg;base64," + str(encoded_string)[2:-1]
            print("Uploading to web...")
            visitHTTP(str(id), image, date.strftime("%d/%m/%Y %H:%M:%S"))

            #Set up a write transaction that sends the command to measure temperature
            cmd_meas_temp = smbus2.i2c_msg.write(si7021_ADD,[si7021_READ_TEMPERATURE])

            #Set up a read transaction that reads two bytes of data
            read_result = smbus2.i2c_msg.read(si7021_ADD,2)

            #Execute the two transactions with a small delay between them
            bus.i2c_rdwr(cmd_meas_temp)
            time.sleep(0.1)
            bus.i2c_rdwr(read_result)

            #convert the result to an int
            temperature = int.from_bytes(read_result.buf[0]+read_result.buf[1],'big')
            temperature = temperature*175.72/65536-46.85
            print("current temp: " + str(temperature)[0:4])
        #green led on when face id detect
        GPIO.output(18,GPIO.HIGH)
        GPIO.output(16,GPIO.LOW)
        time.sleep(1)        

    k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break

# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()

GPIO.output(18,GPIO.LOW)
GPIO.output(16,GPIO.LOW)
# release GPIO 
GPIO.cleanup()

