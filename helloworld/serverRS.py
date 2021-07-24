import socket
SERVER_HOST = "localhost"
SERVER_PORT = 1991
# send 1024 (1kb) a time (as buffer size)
BUFFER_SIZE = 1024
# create a socket object
s = socket.socket()
# bind the socket to all IP addresses of this host
s.bind((SERVER_HOST, SERVER_PORT))
s.listen(5)
print(f"Listening as {SERVER_HOST}:{SERVER_PORT} ...")
client_socket, client_address = s.accept()
print(f"{client_address[0]}:{client_address[1]} Connected!")

# just sending a message, for demonstration purposes
message = "Hello and Welcome".encode()
client_socket.send(message)

while True:
    # get the command from prompt
    command = input("Enter the command you wanna execute:")
    # send the command to the client
    client_socket.send(command.encode())
    if command.lower() == "exit":
        # if the command is exit, just break out of the loop
        break
    # retrieve command results
    results = client_socket.recv(BUFFER_SIZE).decode()
    # print them
    print(results)
# close connection to the client
client_socket.close()
# close server connection
s.close()