import socket
from datetime import datetime

s = socket.socket()
host = "localhost"
port = 50007
username = ""
client_text = '''
,,    ,,                               
  .g8"""bgd `7MM    db                         mm    
.dP'     `M   MM                               MM    
dM'       `   MM  `7MM   .gP"Ya  `7MMpMMMb.  mmMMmm  
MM            MM    MM  ,M'   Yb   MM    MM    MM    
MM.           MM    MM  8M""""""   MM    MM    MM    
`Mb.     ,'   MM    MM  YM.    ,   MM    MM    MM    
  `"bmmmd'  .JMML..JMML. `Mbmmd' .JMML  JMML.  `Mbmo
'''
def loop():
    while True:
        message_input = input("")
        if message_input.lower() == "quit":
            break
        msg = username
        current_time = datetime.now()
        msg += (":" + message_input + ":" + current_time.strftime("%H:%M:%S"))
        s.send(msg.encode())

        print("wating for server message")
        data = s.recv(1024)
        print("server:", data.decode())

def connect(username):
    try:
        print("connecting")
        s.connect((host,port))
        print("connected as " + username)
        loop()
    except:
        trying=input("couldnt connect to server, try again? (y) ")
        if trying == "y":
            connect(username)

print(client_text)
username = input("enter username: ")
connect(username)

s.close()
