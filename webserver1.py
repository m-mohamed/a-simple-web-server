import socket

HOST, PORT = "", 8888

# socket() creates a socket object
# AF_INET refers to the adress family ipv4.
# SOCK_STREAM means that it is a TCP socket
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# bind() is used to associate the socket with a specific network interface and port number:
listen_socket.bind((HOST, PORT))

# listen() enables a server to accept() connections
listen_socket.listen(1)

print(f"Serving HTTP on {PORT} ...")
while True:
    # accept() blocks and waits for an incoming connection.
    client_connection, client_address = listen_socket.accept()
    # recv() This reads whatever data the client sends
    request_data = client_connection.recv(1024)
    print(request_data.decode("utf-8"))

    http_response = b"""\
HTTP/1.1 200 OK

Hello, World!
"""
    # sendall() ecchos back the data sent
    client_connection.sendall(http_response)
    # close() closes the socket at the end of the block.
    client_connection.close()
