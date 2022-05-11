
from mat.ble.bleak_beta.logger_mat import LoggerMAT


def list_files():
    cla = LoggerMAT
    mac = '11:22:33:44:55:66'
    lc = cla()
    lc.ble_connect(mac)
    rv = lc.ble_cmd_dir()
    print('\tparsed ls: {}'.format(rv))
    lc.ble_disconnect()
    lc.ble_bye()


if __name__ == "__main__":
    list_files()
