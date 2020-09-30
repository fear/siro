import socket
import const

multicast_group = const.MULTICAST_GRP
server_address = ('', const.CALLBACK_PORT)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(server_address)

mreq = socket.inet_aton(const.MULTICAST_GRP) + socket.inet_aton("10.0.0.187")

sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

# Receive/respond loop
while True:
    msg = sock.recv(1024)
    print(msg)
