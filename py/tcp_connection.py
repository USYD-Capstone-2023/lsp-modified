import socket
import struct
import time
import sys

#Huys
#s_ip = '100.83.66.107'

# Anthony
#s_ip = '100.83.127.39'
#s_ip = '100.117.127.225'

#Tom
#s_ip = '100.108.85.189'

s_port = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def connect():

    with open('py/configIp.txt', 'r') as file:
        # Read the first line and store it in a variable
        s_ip = file.readline()
        #print(s_ip)


    try:
        s.connect((s_ip.strip('\n'), s_port))
        print('Connected to server')
        
        #with open("music/sample/Samantha_Jade_-_Firestarter.mp3", "rb") as file:
        #    print(sys.argv[2])
        with open(str(sys.argv[2]), "rb") as file:
            while True:
                mp3_file=file.read(1024)
                if not mp3_file:
                    break
                s.sendall(mp3_file)
        time.sleep(1)
        end_signal="SIGNAL_END_MP3"
        s.sendall(end_signal.encode('utf-8'))
    except socket.error as e:
        print(str(e))
        exit(1)

def send_data(pin, pwd):
    try:
        if not isinstance(pwd, int):
            return
        pin=struct.pack('B',pin)
        pwd=struct.pack('B',pwd)
        s.sendall(pin)  # Convert data to bytes and send it
        s.sendall(pwd)    
    except socket.error as e:
        print(str(e))
        exit(1)

def send_music_flag():
    # NOTE This is a temp solution since we dont have 255 pins yet
    audio_flag = struct.pack('B',255)
    s.sendall(audio_flag)
    s.sendall(audio_flag)

#    with open("music/sample/ovenrake_deck-the-halls.mp3", "rb") as file:
#        mp3_file=file.read() s.sendall(mp3_file)

def get_data(): 
    try:
        data = s.recv(1024)
        print('Received', repr(data))
        return data
    except socket.error as e:
        print(str(e))
        return None

def disconnect():
    try:
        s.close()
        print('Disconnected from server')
    except socket.error as e:
        print(str(e))
        exit(1)
