from ble.ble_macs import get_mac
from mat.ble.bleak_beta.logger_do2 import LoggerDO2


def list_files(cla):
    mac = get_mac(cla)
    lc = cla()
    lc.ble_connect(mac)
    lc.ble_cmd_dir()
    lc.ble_disconnect()
    lc.ble_bye()


if __name__ == "__main__":
    list_files(LoggerDO2)