from _macs import get_mac
from ble.bluepy.xmlrpc.simple import simple
from mat.ble.bluepy.xc_ble_lowell import XS_BLE_CMD_GTM


mac = get_mac()


def get_time():
    simple(XS_BLE_CMD_GTM, mac)


if __name__ == '__main__':
    get_time()
