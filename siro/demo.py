import json
import const

from .siro import RadioMotor, Bridge, Connector


def aprint(some_text) -> None:
    print(some_text)


def main1(key, addr) -> None:
    Connector().start_cli(key, addr)


def main2(key) -> None:
    bridge: Bridge = Connector.bridge_factory(key)

    bridge.print_device_info()
    devices = bridge.get_devices()
    device: RadioMotor = devices[0]

    device.move_up()
    device.move_down()
    device.move_to_position(40)
    device.move_to_position(35)
    device.move_stop()
    device.get_status()


if __name__ == '__main__':
    config_ = json.load(open('config.json'))
    main1(config_['key'], config_['bridge'])
