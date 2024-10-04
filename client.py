import socket


# Define client socket
def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 65432))

    while True:
        print("\nSelect an option:")
        print("1: Say Hello")
        print("2: File Transfer")
        print("3: Calculator")
        print("4: Exit")

        choice = input("Enter your choice: ")
        client.send(choice.encode())

        if choice == '1':
            # Say Hello
            response = client.recv(1024).decode()
            print(f"Server: {response}")

        elif choice == '2':
            # File Transfer
            filename = input("Enter the filename to download: ")
            client.send(filename.encode())
            response = client.recv(1024).decode()

            if response == "File exists":
                with open(f"downloaded_{filename}", 'wb') as file:
                    while True:
                        data = client.recv(1024)
                        if not data:
                            break
                        file.write(data)
                print(f"File {filename} downloaded successfully.")
            else:
                print("File does not exist on server.")

        elif choice == '3':
            # Calculator
            expression = input("Enter a mathematical expression (e.g., 5 + 3 * 2): ")
            client.send(expression.encode())
            result = client.recv(1024).decode()
            print(f"Result: {result}")

        elif choice == '4':
            # Exit
            print("Exiting...")
            client.close()
            break


if __name__ == "__main__":
    start_client()
