import json
from socket import (
    AF_INET,
    IPPROTO_IP,
    IP_ADD_MEMBERSHIP,
    SOCK_DGRAM,
    inet_aton,
    socket,
)
import asyncio


class AsyncTest:

    def __init__(self):
        self._callback_address = self._ident_callback_address()
        self._sock = None
        self._init_socket()

    @staticmethod
    def _ident_callback_address(callback_address: str = "") -> str:
        if callback_address == '':
            s = socket(AF_INET, SOCK_DGRAM)
            s.connect(("208.67.222.222", 80))
            address_ = s.getsockname()[0]
            s.close()
        else:
            address_ = callback_address
        return address_

    def listen(self) -> None:
        # noinspection PyBroadException
        msg = self._sock.recv(1024)
        data = json.loads(msg.decode('utf-8'))
        print(data)

    def _init_socket(self) -> None:
        try:
            s = socket(AF_INET, SOCK_DGRAM)
            s.bind(('', 32101))
            mreq = inet_aton("238.0.0.18") + inet_aton(self._callback_address)
            s.setsockopt(IPPROTO_IP, IP_ADD_MEMBERSHIP, mreq)
            self._sock = s
        except Exception:
            raise

    async def listen_async(self, loop_):
        await loop_.sock_recv(self._sock, 1024)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    myclass = AsyncTest()
    myclass.listen()

    loop.run_until_complete()

    loop.run_forever(myclass.listen_async(loop))
    loop.close()
    # loop.run_until_complete(wait_tasks)
