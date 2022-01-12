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
    devices: list = bridge.get_devices()

    device: RadioMotor = devices[0]
    print(device.move_up())
    await asyncio.sleep(2)
    print(device.get_status())
    await asyncio.sleep(2)
    print(device.move_down())
    await asyncio.sleep(1)
    print(device.move_stop())

if __name__ == '__main__':
    config_ = json.load(open('config.json'))
    key_ = config_['key']

    loop = asyncio.get_event_loop()
    future = loop.create_task(
        class_usage_demo(key_, loop)
    )
    loop.run_until_complete(future)
