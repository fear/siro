import json

from siro import (
    RadioMotor,
    Bridge,
    Helper
)


# noinspection PyShadowingNames
def cli_demo(key_, addr_="") -> None:
    Helper().start_cli(key_, addr_)


# noinspection PyShadowingNames
def class_usage_demo(key_) -> None:
    bridge: Bridge = Helper.bridge_factory(key_)

    devices: list = bridge.get_devices()
    device: RadioMotor = devices[0]

    device.move_up()
    device.move_down()
    device.move_to_position(40)
    device.move_to_position(35)
    device.move_stop()
    device.get_status()


if __name__ == '__main__':
    config_ = json.load(open('config.json'))
    key_ = config_['key']

    cli_demo(key_)
    # class_usage_demo(key_)
