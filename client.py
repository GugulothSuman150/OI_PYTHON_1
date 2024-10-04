import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"\nServer: {message}")
        except:
            print("Connection closed.")
            break

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 12345))  # Connect to the server

    thread = threading.Thread(target=receive_messages, args=(client,))
    thread.start()

    while True:
        message = input("You: ")
        client.send(message.encode('utf-8'))

if __name__ == "__main__":
    main()
