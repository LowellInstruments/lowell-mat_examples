from ble.ble_macs import MAC_LOGGER_MAT1_0, get_mac
from mat.ble.bleak_beta.logger_mat import LoggerMAT


def stop():
    cla = LoggerMAT
    mac = get_mac(cla)
    lc = cla()
    lc.ble_connect(mac)
    lc.ble_cmd_stp()
    lc.ble_disconnect()
    lc.ble_bye()


if __name__ == "__main__":
    stop()
