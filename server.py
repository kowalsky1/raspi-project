import socket

HOST = ''
PORT = 50007

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

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
