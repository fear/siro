#!python3

import json
import asyncio

from siro import (
    RadioMotor,
    Bridge,
    Helper
)


# noinspection PyShadowingNames
async def class_usage_demo(key_, loop) -> None:
    bridge: Bridge = await Helper.bridge_factory(key_, loop=loop)
    listen = asyncio.create_task(bridge.listen(loop))

    await listen

    device = bridge.get_device_by_mac('98f4ab8932a40008')
    print('Warte 3 Sekunden')
    await asyncio.sleep(2)

    print('Move Down...')
    device.move_down()

    print('Statusabfrage:')
    print(device.get_status())

    print('Warte 5 Sekunden')
    await asyncio.sleep(5)

    print('Move Down...')
    device.move_up()

    print('Warte 5 Sekunden')
    await asyncio.sleep(5)

    print('Stop...')
    device.move_stop()

    print('Warte 5 Sekunden')
    await asyncio.sleep(5)

    print('Fahre auf position 10% geschlossen')
    device.move_to_position(10)

if __name__ == '__main__':
    config_ = json.load(open('config.json'))
    key_ = config_['key']

    loop = asyncio.get_event_loop()
    future = loop.create_task(
        class_usage_demo(key_, loop)
    )
    loop.run_until_complete(future)

