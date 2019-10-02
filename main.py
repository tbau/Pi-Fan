import Adafruit_DHT
import threading
from flask_cors import CORS, cross_origin
from flask import jsonify
import io
import picamera
import logging
import socketserver
from threading import Condition
from http import server
import RPi.GPIO as gpio
import urllib.parse
from flask import Flask
from flask import request
from time import sleep

app = Flask(__name__)

cors = CORS(app, resources={r'/*':{"origins":'*'}})

on=False
speed="full"
gpio.setmode(gpio.BOARD)

gpio.setup(12,gpio.OUT)
gpio.output(12,0)

sensor=Adafruit_DHT.DHT11
gpin = 17

f = open("page1.html","r")
t = ""
for i in f:
 t = t + i
PAGE1 = t

f.close()

f = open("page2.html","r")
t = ""
for i in f:
 t = t + i
PAGE2 = t

f.close()
t=""


mediumThread = None
@app.route('/')
def toggle():
 global on
 if on:
  content = PAGE1.encode('utf-8')+str("on").encode('utf-8')+PAGE2.encode('utf-8')
 else:
  content = PAGE1.encode('utf-8')+str("off").encode('utf-8')+PAGE2.encode('utf-8')
 return content
@app.route('/set.html')
def set():
 set = request.args.get('set')
 global on
 global mediumThread
 global speed
 if set=="ON":
  if speed=="medium":
   mediumThread = threading.Thread(target=loop)
   mediumThread.looping=True
   mediumThread.start()
  else:
   if not mediumThread == None:
    mediumThread.looping=False;
   gpio.output(12,1)
  on=True
 elif set=="OFF":
  on=False
  if not mediumThread == None:
   mediumThread.looping=False;
  sleep(1)
  gpio.output(12,0)
 return " "

def loop():
 temp = on
 t = threading.currentThread()
 print('in thread')
 try:
  gpio.output(12,1)
  while getattr(t, "looping",True):
   gpio.output(12,1)
   sleep(.00001)
   gpio.output(12,0)
   sleep(.00001)
 except:
  pass 
 return " "

@app.route('/setSpeedMedium')
def setSpeedMedium():
 global on
 global mediumThread
 global speed
 
 speed = "medium"
 if on:   
   gpio.output(12,0)
   mediumThread = threading.Thread(target=loop)
   mediumThread.looping=True
   mediumThread.start()
    
 return " "
  
 
@app.route('/setSpeedFull')
def setSpeedFull():
 global on
 global mediumThread
 global speed
 if not mediumThread == None:
  mediumThread.looping=False
  
 speed="full"
 if on:
  sleep(2)
  gpio.output(12,1)
 
 return " "
   
@app.route('/getspeed')
def getspeed():
 global speed
 a = speed
 if a=="full":
  a="Full"
 if a=="medium":
  a="Medium"
 return jsonify("{speed:"+a+"}");
    



@app.route('/state')
@cross_origin(supports_credentials=True, headers=['Content-Type','Authorization'])
def state():
 global on
 if on:
  return jsonify("{status: on}")
 else:
  return jsonify("{status: off}")
if __name__ =='__main__':
 app.run(host='0.0.0.0')
@app.route('/temp')
def temp():
  humidity, temperature = Adafruit_DHT.read_retry(sensor, gpin)
  if humidity is not None and temperature is not None:
   return 'Temp={0:0.1f}*F  Humidity={1:0.1f}%'.format(temperature*1.8+32, humidity)
  else:
    print('Failed to get reading. Try again!')
 


 
