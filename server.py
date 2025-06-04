import socket

# Server configuration
HOST = '127.0.0.1'  # localhost
PORT = 8080

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set socket option to reuse address
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind the socket to the address
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen(1)
print(f"Server listening on {HOST}:{PORT}...")

# Accept a connection
client_socket, client_address = server_socket.accept()
print(f"Connected to client at {client_address}")

# Receive data from the client
data = client_socket.recv(1024)
print(f"Received message: {data.decode()}")

# Send acknowledgment back to client
response = "Message received!"
client_socket.send(response.encode())

# Close the connection
client_socket.close()
server_socket.close() 