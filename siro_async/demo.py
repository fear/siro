import json
import const

from siro import Connector, Bridge, RadioMotor


def aprint(some_text) -> None:
    print(some_text)


def main1(key, addr) -> None:
    Connector().start_cli(key, addr)


def main2(key) -> None:
    bridge: Bridge = Connector.bridge_factory(key)

    bridge.print_variable()
    # devices = await bridge.get_devices()
    # device: RadioMotor = devices[0]
    #
    # await asyncio.gather(
    #     aprint(await device.up()),
    #     # device.down(),
    #     # device.position(40),
    #     # device.position(35),
    #     # device.stop(),
    #     # device.get_status(),
    # )


if __name__ == '__main__':
    config_ = json.load(open('config.json'))
    main1(config_['key'], config_['bridge'])
