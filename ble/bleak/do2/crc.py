
from mat.ble.bleak_beta.logger_do2 import LoggerDO2


def crc():
    mac = '11:22:33:44:55:66'
    lc = LoggerDO2()
    lc.ble_connect(mac)
    # DIR before so you know a valid filename
    filename = 'dummy_73286.lid'
    lc.ble_cmd_crc(filename)
    lc.ble_disconnect()
    lc.ble_bye()


if __name__ == "__main__":
    crc()
