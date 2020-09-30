import socket

multicast_group = '238.0.0.18'
server_address = ('', 32101)


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind(server_address)

mreq = socket.inet_aton(multicast_group) + socket.inet_aton("10.0.0.187")

sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

# Receive/respond loop
while True:
    msg = sock.recv(1024)
    print(msg)
