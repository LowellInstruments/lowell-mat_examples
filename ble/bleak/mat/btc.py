from ble.ble_macs import get_mac
from mat.ble.bleak_beta.logger_mat import LoggerMAT


def btc():
    cla = LoggerMAT
    mac = get_mac(cla)
    lc = cla()
    lc.ble_connect(mac)
    lc.ble_cmd_btc()
    lc.ble_disconnect()
    lc.ble_bye()


if __name__ == "__main__":
    btc()
