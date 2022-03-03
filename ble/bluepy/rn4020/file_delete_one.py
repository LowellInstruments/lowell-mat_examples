from _macs import get_mac
from mat.ble.bluepy.rn4020_logger_controller import LoggerControllerRN4020


def file_del(file_name):
    mac = get_mac()
    lc = LoggerControllerRN4020(mac)

    if lc.open():
        rv = lc.ble_cmd_stp()
        print('stop', rv)
        rv = lc.ble_cmd_del(file_name)
        print('file deleted', rv)
    else:
        print('{} connection error'.format(__name__))
    lc.close()


if __name__ == '__main__':
    s = 'a.lid'
    file_del(s)
