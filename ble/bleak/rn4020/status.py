
from mat.ble.bleak_beta.logger_mat import LoggerMAT


def status():
    cla = LoggerMAT
    mac = '11:22:33:44:55:66'
    lc = cla()
    lc.ble_connect(mac)
    lc.ble_cmd_sts()
    lc.ble_disconnect()
    lc.ble_bye()


if __name__ == "__main__":
    status()
