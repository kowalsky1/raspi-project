import socket

s = socket.socket()
host = "localhost"
port = 50007
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

print(client_text)
username = input("enter username: ")

print("connecting")
s.connect((host, port))
print("connected")

while True:
    msg = input("")
    if msg.lower() == "quit":
        break

    s.send(username.encode())
    s.send(msg.encode())

    data = s.recv(1024)
    print("server:", data.decode())

s.close()
