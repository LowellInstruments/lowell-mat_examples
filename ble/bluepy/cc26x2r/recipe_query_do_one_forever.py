import datetime
import time

import yaml
from mat.ble.bluepy.cc26x2r_logger_controller import LoggerControllerCC26X2R
import os


def _is_do_sensor_working(mac):
    lc = LoggerControllerCC26X2R(mac)
    if lc.open():
        s = '\n{}\n'.format(mac)
        s += '{}\n'.format(str(datetime.datetime.now()))
        rv = lc.ble_cmd_stp()
        s += 'stop: {}\n'.format(rv)
        rv = lc.ble_cmd_bat()
        s += 'bat: {}\n'.format(rv)
        rv = lc.ble_cmd_gdo()
        s += 'gdo: {}\n'.format(rv)

        print(s)
        with open('_test.txt', 'a') as f:
            f.write(s)

    else:
        print('{} connection error'.format(__name__))
        rv = False
    lc.close()
    return rv


def query_do_one_forever():
    while 1:
        # 04:EE:03:73:87:22: 2002019
        _is_do_sensor_working('04:EE:03:73:87:22')
        time.sleep(60)


if __name__ == '__main__':
    query_do_one_forever()
