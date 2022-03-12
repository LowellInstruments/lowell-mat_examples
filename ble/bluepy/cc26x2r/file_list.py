from mat.ble.bluepy.cc26x2r_logger_controller import LoggerControllerCC26X2R
from _macs import get_mac


def file_list():

    # mac = get_mac()
    mac = '60:77:71:22:C8:49'
    lc = LoggerControllerCC26X2R(mac)

    if lc.open():
        rv = lc.ble_cmd_stp()
        print('stop', rv)
        rv = lc.ble_cmd_dir_ext('*')
        print('list all files: {}\n'.format(rv))
        return rv
    else:
        print('{} connection error'.format(__name__))
    lc.close()


if __name__ == '__main__':
    file_list()
