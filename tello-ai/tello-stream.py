import socket

udp_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

udp_socket.bind(('', 11111))

while True:
    try:
        print("we will recieve data: \n")
        data, server = udp_socket.recvfrom(1024)
        print("message : ", data.decode())
    except Exception as err:
        print("Error occurred")
        print(err)
        udp_socket.close()
        break
