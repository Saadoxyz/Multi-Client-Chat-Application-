import socket
import threading

HOST = '127.0.0.1'  # Same as server
PORT = 5555

# Ask user for department and name
department = input("Enter your department: ").strip()
name = input("Enter your name: ").strip()

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

# Send department and name to server
client.send(department.encode())
client.send(name.encode())


def receive_messages():
    """
    Thread function to receive and print messages from server.
    """
    while True:
        try:
            message = client.recv(1024).decode()
            if message:
                print(message)
            else:
                # Server disconnected
                print("Disconnected from server.")
                break
        except:
            print("Error receiving message.")
            break


def send_messages():
    """
    Thread function to send messages typed by the user.
    """
    while True:
        msg = input()
        if msg:
            try:
                client.send(msg.encode())
            except:
                print("Error sending message.")
                break


# Start threads for sending and receiving
recv_thread = threading.Thread(target=receive_messages)
recv_thread.daemon = True  # This thread will exit when main program exits
recv_thread.start()

send_thread = threading.Thread(target=send_messages)
send_thread.daemon = True
send_thread.start()

# Keep main thread alive so the program doesn’t exit
recv_thread.join()
send_thread.join()
