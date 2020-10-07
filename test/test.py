import asyncio
import socket


class SiroProtocol(asyncio.DatagramProtocol):
    def __init__(self):
        self.a = "new"
        print('init')

    def connection_made(self, transport):
        self.transport = transport
        print('Connection Made')

    def connection_lost(self, exc):
        print('connection lost')

    def datagram_received(self, data, addr):
        message = data.decode()
        print('Received %r from %s' % (message, addr))
        # print('Send %r to %s' % (message, addr))
        # self.transport.sendto(data, addr)


def init_socket() -> socket.socket:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind(('', 32101))
        mreq = socket.inet_aton('238.0.0.18') + socket.inet_aton('10.0.0.187')
        s.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
        s.setblocking(False)
        return s
    except Exception:
        raise


async def get_device_list(sock):
    import json

    await asyncio.sleep(5)

    addr = ('10.0.0.192', 32100)
    data = json.dumps({
        'msgType': 'GetDeviceList',
        'msgID': get_timestamp()}
    )
    sock.sendto(data.encode(), addr)


def get_timestamp() -> str:
    from datetime import datetime
    return datetime.now().strftime("%Y%m%d%H%M%S%f")[0:17]


async def listen(sock, loop):
    print("Starting UDP server")

    # One protocol instance will be created to serve all
    # client requests.
    transport, protocol = await loop.create_datagram_endpoint(
        SiroProtocol,
        sock=sock
    )
    try:
        await asyncio.sleep(60)  # Serve for 1 minute.
    finally:
        print("close transport")
        transport.close()


async def say_after(delay, what="some delayed text..."):
    await asyncio.sleep(delay)
    print(what)


async def main(loop):
    sock = init_socket()

    t_listen = asyncio.create_task(listen(sock, loop))
    t_out = asyncio.create_task(say_after(10))
    t_list = asyncio.create_task(get_device_list(sock))

    await t_listen
    await t_out
    await t_list

loop = asyncio.get_event_loop()
loop.create_task(main(loop))
loop.run_forever()


