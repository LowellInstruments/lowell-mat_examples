from _macs import get_mac
from mat.ble.bleak_beta.logger_mat import LoggerMAT


def stop():
    cla = LoggerMAT
    mac = get_mac()
    lc = cla()
    lc.ble_connect(mac)
    lc.ble_cmd_stp()
    lc.ble_disconnect()
    lc.ble_bye()


if __name__ == "__main__":
    stop()
