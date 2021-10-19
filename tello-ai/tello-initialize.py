import socket

tello_ip = "192.168.10.1"
tello_port = 8889

udp_server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
tello_address = (tello_ip, tello_port)
udp_server_socket.bind(('', 9000))

print("Tello UDP server up and listening")

while True:
    try:
        message = input('')
        if not message:
            break
        if 'end' in message:
            udp_server_socket.close()
            break
        message = message.encode()
        print("message : ", message)
        sent = udp_server_socket.sendto(message, tello_address)
    except Exception as err:
        print("Error occurred")
        print(err)
        udp_server_socket.close()
        break


