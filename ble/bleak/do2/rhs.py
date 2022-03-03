from _macs import get_mac
from mat.ble.bleak_beta.logger_do2 import LoggerDO2


def rhs():
    mac = get_mac()
    lc = LoggerDO2()
    lc.ble_connect(mac)
    lc.ble_cmd_rhs()
    lc.ble_disconnect()
    lc.ble_bye()


if __name__ == "__main__":
    rhs()
