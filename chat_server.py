import socket
import threading
import datetime

# Server settings
HOST = '127.0.0.1'  # localhost - your own computer
PORT = 5555         # Port number (can be anything free)

# Dictionary to store connected clients
# Format: {client_socket: (department, name)}
clients = {}

# Log file to save chat history
LOG_FILE = "chat_log.txt"


def broadcast(message, sender_socket=None):
    """
    Send message to all clients except sender (if given).
    """
    for client_sock in clients:
        if client_sock != sender_socket:
            try:
                client_sock.send(message.encode())
            except:
                # If sending fails, remove client
                client_sock.close()
                del clients[client_sock]


def handle_client(client_sock):
    """
    Handle communication with a connected client.
    """
    try:
        # Step 1: Receive department and name from client
        department = client_sock.recv(1024).decode().strip()
        name = client_sock.recv(1024).decode().strip()

        # Save client info
        clients[client_sock] = (department, name)

        # Notify everyone new client joined
        join_msg = f"{department} {name} joined the chat."
        print(join_msg)
        broadcast(join_msg, client_sock)

        while True:
            # Receive message from client
            msg = client_sock.recv(1024).decode()
            if not msg:
                # Client disconnected
                break

            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            # Bonus: Handle /list command
            if msg.strip() == '/list':
                user_list = ", ".join(f"{dep} {nm}" for dep, nm in clients.values())
                client_sock.send(f"[{timestamp}] Connected users: {user_list}".encode())
                continue

            # Format full message
            full_msg = f"[{timestamp}] {department} {name}: {msg}"
            print(full_msg)

            # Save message to log file
            with open(LOG_FILE, "a") as log:
                log.write(full_msg + "\n")

            # Broadcast to other clients
            broadcast(full_msg, client_sock)

    except Exception as e:
        print(f"Error with client {clients.get(client_sock, '')}: {e}")

    finally:
        # Clean up after client disconnects
        if client_sock in clients:
            left_msg = f"{clients[client_sock][0]} {clients[client_sock][1]} left the chat."
            print(left_msg)
            broadcast(left_msg, client_sock)
            del clients[client_sock]
        client_sock.close()


def start_server():
    """
    Start the TCP server and listen for connections.
    """
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print(f"Server started on {HOST}:{PORT}")

    while True:
        client_sock, addr = server.accept()
        print(f"New connection from {addr}")
        threading.Thread(target=handle_client, args=(client_sock,)).start()


if __name__ == "__main__":
    start_server()
