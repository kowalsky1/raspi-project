import socket

HOST = ''
PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
server_text = '''

 .M"""bgd                                                
,MI    "Y                                                
`MMb.      .gP"Ya  `7Mb,od8 `7M'   `MF' .gP"Ya  `7Mb,od8 
  `YMMNq. ,M'   Yb   MM' "'   VA   ,V  ,M'   Yb   MM' "' 
.     `MM 8M""""""   MM        VA ,V   8M""""""   MM     
Mb     dM YM.    ,   MM         VVV    YM.    ,   MM     
P"Ybmmd"   `Mbmmd' .JMML.        W      `Mbmmd' .JMML.
'''

print(server_text)
print("Server listening...")
conn, addr = s.accept()
print('Connected by', addr)

while True:
    data = conn.recv(1024)
    if not data:
        break


    message = data.decode()          # bytes → string
    print(addr, message)


conn.close()
