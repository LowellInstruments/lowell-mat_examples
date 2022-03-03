from _macs import get_mac
from ble.bluepy.xmlrpc.simple import simple
from mat.ble.bluepy.xc_ble_lowell import XS_BLE_CMD_STS


mac = get_mac()


def status():
    simple(XS_BLE_CMD_STS, mac)


if __name__ == '__main__':
    status()
