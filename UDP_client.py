import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('127.0.0.1', 65432)

filename = input("Enter the filename to download: ")
client.sendto(filename.encode(), server_address)

data, _ = client.recvfrom(1024)
if data.decode() == "File exists":
    with open(f"downloaded_{filename}", 'wb') as file:
        while True:
            data, _ = client.recvfrom(1024)
            if data == b'EOF':
                break
            file.write(data)
    print(f"File {filename} downloaded successfully.")
else:
    print("File does not exist on server.")
