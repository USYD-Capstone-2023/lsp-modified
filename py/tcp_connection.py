import socket
import struct

#Huys 
s_ip = '100.83.66.107'

# Anthony
#s_ip = '100.83.127.39'
#s_ip = '100.117.127.225'

s_port = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def connect():
    try:
        s.connect((s_ip, s_port))
        print('Connected to server')
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
