from _macs import get_mac
from mat.ble.bleak_beta.logger_do2 import LoggerDO2


def delete_file(file_name):
    mac = get_mac()
    lc = LoggerDO2()
    lc.ble_connect(mac)
    lc.ble_cmd_del(file_name)
    lc.ble_disconnect()
    lc.ble_bye()


if __name__ == "__main__":
    delete_file('dummy_750.lid')
