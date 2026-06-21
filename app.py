import socket

target = input("Enter IP Address: ")

for port in range(1, 101):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)

    if s.connect_ex((target, port)) == 0:
        print("Port", port, "is Open")

    s.close()