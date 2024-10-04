import socket
import threading

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"\nClient: {message}")
            response = input("You: ")
            client_socket.send(response.encode('utf-8'))
        except:
            print("Connection closed.")
            break

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 12345))  # Bind to all interfaces on port 12345
    server.listen(1)
    print("Server is listening for incoming connections...")

    client_socket, addr = server.accept()
    print(f"Connection from {addr} has been established!")

    handle_client(client_socket)

if __name__ == "__main__":
    main()
