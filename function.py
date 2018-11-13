from picamera import PiCamera
import RPi.GPIO as GPIO
import time, smtplib, random, thread
from bottle import route, run, template, static_file

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GMAIL_USER = #'user@gmail.com'
GMAIL_PASS = #'password'
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

IP = #'11.111.111.111'
FILE_LOCATION = #'/home/user/BirdFeeder/'

camera = PiCamera()
text_file = open('numPics.txt', 'r+')
numPics = int(text_file.readline())
camera.rotation = 270

@route('/')
def serve_homepage():
    return template(FILE_LOCATION + 'main.html')

@route('/getNumPics')
def getNumPics():
    return str(numPics)

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./pics')

def send_email(recipient, subject, text):
    smtpserver = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(GMAIL_USER, GMAIL_PASS)
    header = 'BCC:' + recipient + '\n' + 'From: ' + GMAIL_USER
    header = header + '\n' + 'Subject:' + subject + '\n'
    msg = header + '\n' + text + '\n\n'
    smtpserver.sendmail(GMAIL_USER, recipient, msg)
    smtpserver.close()

def mainLoop(i):
    global numPics
    feedTypes = ['Sunflower', 'Safflower', 'Cracked Corn', 'Peanut']

    is17old = True
    is18old = True

    while True:
        is17 = GPIO.input(17)
        is18 = GPIO.input(18)
        if is17old == False and is17 == True:
            print('Sending Email...')
            send_email(GMAIL_USER, 'Refill Feed', 'You should buy some ' + feedTypes[random.randint(0, len(feedTypes) - 1)] + ' Seed.')
            print('Email Sent')
        if is18old == True and is18 == False:
            print('Take Picture ' + str(numPics))
            camera.capture(FILE_LOCATION + 'pics/pic' + str(numPics) + '.jpg')
            numPics = numPics + 1
        text_file.seek(0)
        text_file.write(str(numPics))
        text_file.truncate()
        is17old = is17
        is18old = is18
        time.sleep(0.2)

thread.start_new_thread(mainLoop, (None,))

run(host = IP,  port = 80)
