import socket
import os

# Define server socket
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 65432))
    server.listen(5)
    print("Server is listening on 127.0.0.1:65432")

    while True:
        client_socket, addr = server.accept()
        print(f"Connection established with {addr}")

        while True:
            # Receive the operation choice
            choice = client_socket.recv(1024).decode()

            if choice == '1':
                # Say Hello
                client_socket.send("Hello from Server!".encode())

            elif choice == '2':
                # File Transfer
                filename = client_socket.recv(1024).decode()
                if os.path.exists(filename):
                    client_socket.send("File exists".encode())
                    with open(filename, 'rb') as file:
                        data = file.read(1024)
                        while data:
                            client_socket.send(data)
                            data = file.read(1024)
                    print(f"File {filename} sent successfully")
                else:
                    client_socket.send("File does not exist".encode())

            elif choice == '3':
                # Calculator
                expression = client_socket.recv(1024).decode()
                try:
                    result = eval(expression)
                    client_socket.send(str(result).encode())
                except:
                    client_socket.send("Invalid expression".encode())

            elif choice == '4':
                # Close connection
                print("Closing connection with client.")
                client_socket.close()
                break

if __name__ == "__main__":
    start_server()
