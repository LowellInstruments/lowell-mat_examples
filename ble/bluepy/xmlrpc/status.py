
from ble.bluepy.xmlrpc.simple import simple
from mat.ble.bluepy.xc_ble_lowell import XS_BLE_CMD_STS


mac = '11:22:33:44:55:66'


def status():
    simple(XS_BLE_CMD_STS, mac)


if __name__ == '__main__':
    status()
