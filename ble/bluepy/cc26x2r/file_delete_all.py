import time

from ble.bluepy.cc26x2r.file_list import file_list
from mat.ble.bluepy.cc26x2r_logger_controller import LoggerControllerCC26X2R
from _macs import get_mac


def file_del_all(d: dict):

    mac = get_mac()
    lc = LoggerControllerCC26X2R(mac)

    if lc.open():
        # d: {'1234567_low_20220110_112843.lid': 2182, 'MAT.cfg': 188}
        for i in d.keys():
            if i == 'MAT.cfg':
                continue
            rv = lc.ble_cmd_del(i)
            time.sleep(2)
            print('file delete {}: {}\n'.format(i, rv))
    else:
        print('{} connection error'.format(__name__))
    lc.close()


if __name__ == '__main__':
    fl = file_list()
    file_del_all(fl)
