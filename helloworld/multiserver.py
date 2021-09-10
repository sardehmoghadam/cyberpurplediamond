import socket               # Import socket module
import _thread

def on_new_client(clientsocket,addr):
    while True:
        # get the command from prompt
        command = input("Enter the command you wanna execute:")
        # send the command to the client
        clientsocket.send(command.encode())
        if command.lower() == "exit":
            # if the command is exit, just break out of the loop
            break
        # retrieve command results
        results = clientsocket.recv(BUFFER_SIZE).decode()
        # print them
        print(results)
    clientsocket.close()

s = socket.socket()         # Create a socket object
host = "localhost" # Get local machine name
port = 1991                # Reserve a port for your service.
BUFFER_SIZE = 1024

print('Server started!')
print('Waiting for clients...')

s.bind((host, port))        # Bind to the port
s.listen(5)                 # Now wait for client connection.


while True:
   c, addr = s.accept()     # Establish connection with client.
   print('Got connection from', addr)
   _thread.start_new_thread(on_new_client,(c,addr))
   #Note it's (addr,) not (addr) because second parameter is a tuple
   #Edit: (c,addr)
   #that's how you pass arguments to functions when creating new threads using thread module.
s.close()