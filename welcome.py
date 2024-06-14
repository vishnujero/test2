
import socket

def start_server(host='0.0.0.0', port=3000):
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the host and port
    server_socket.bind((host, port))

    # Enable the server to accept connections (the parameter specifies the backlog size)
    server_socket.listen(5)

    print(f"Server listening on {host}:{port}")

    while True:
        # Establish a connection
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")

        # Receive data from the client
        data = client_socket.recv(1024)
        if data:
            print(f"Received dataa: {data.decode('utf-8')}")

        # Close the client connection
        client_socket.close()

if __name__ == "__main__":
    start_server()
