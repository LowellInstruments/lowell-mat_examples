import time
from ble.ble_macs import MAC_LOGGER_MAT1_0, get_mac
from mat.ble.bleak_beta.logger_mat import LoggerMAT
from mat.ble_utils_shared import utils_mat_convert_data


def get_file():
    cla = LoggerMAT
    mac = get_mac(cla)
    lc = cla()
    lc.ble_connect(mac)

    filename = '2011605_TP_1m_(0).lid'
    size = 326492
    rv = lc.ble_cmd_get(filename)
    data = bytes()
    start = time.perf_counter()
    if rv == b'\n\rGET 00\r\n':
        data = lc.ble_cmd_xmodem(size)
    if data:
        path = '/home/kaz/Downloads/puta.lid'
        if utils_mat_convert_data(data, path, size):
            print('converted OK')
        else:
            print('conversion error')
    else:
        print('xmodem error')

    end = time.perf_counter()
    if data:
        _ = size / (end - start)
        print('speed {} KB/s'.format(_ / 1000))

    lc.ble_disconnect()
    lc.ble_bye()


if __name__ == "__main__":
    get_file()
