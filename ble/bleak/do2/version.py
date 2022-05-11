
from mat.ble.bleak_beta.logger_do2 import LoggerDO2


def get_version():
    mac = '11:22:33:44:55:66'
    lc = LoggerDO2()
    lc.ble_connect(mac)
    lc.ble_cmd_gfv()
    lc.ble_disconnect()
    lc.ble_bye()


if __name__ == "__main__":
    get_version()
