import socket

s = socket.socket()
host = "localhost"
port = 50007
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
