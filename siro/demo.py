#!python3

import asyncio

from siro import (
    RadioMotor,
    Bridge,
    Helper
)


# noinspection PyShadowingNames
async def class_usage_demo(key_, loop) -> None:
    bridge: Bridge = await Helper.bridge_factory(key_, loop=loop)

    await asyncio.create_task(bridge.listen(loop))

    device = bridge.get_device_by_mac('98f4ab8932a40008')

    print('Warte 2 Sekunden')
    await asyncio.sleep(2)

    print('Move Down...')
    device.move_down()

    print('Statusabfrage:')
    print(device.get_status())

    print('Warte 5 Sekunden')
    await asyncio.sleep(5)

    print('Move Down...')
    device.move_up()

    print('Warte 2 Sekunden')
    await asyncio.sleep(2)

    print('Stop...')
    device.move_stop()

    print('Warte 1 Sekunden')
    await asyncio.sleep(1)

    print('Fahre auf position 20%')
    device.move_to_position(20)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    future = loop.create_task(
        class_usage_demo('30b9217c-6d18-4d', loop)
    )

    loop.run_until_complete(future)
