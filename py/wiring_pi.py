import tcp_connection
def wiringPiSetup(*args):
    print("Setting up")
    #tcp_connection.connect()

def wiringPiSetupSys(*args):
    print("called wiringpi setup sys")

def pinMode(pin, pwd):
    print("Pin "+ str(pin) + " set MODE to "+ str(pwd))
    #tcp_connection.send_data(pin, "M" + str(pwd))

def digitalWrite(pin,pwd):
    print("Pin "+ str(pin) + " set to "+ str(pwd))
    #tcp_connection.send_data(pin,pwd)
    pass
