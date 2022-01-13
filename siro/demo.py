#!python3

from siro import (
    Connector
)


# noinspection PyShadowingNames
def cli_demo(key_, addr_="") -> None:
    Connector().start_cli(key_, addr_)


if __name__ == '__main__':
    cli_demo('30b9217c-6d18-4d')
