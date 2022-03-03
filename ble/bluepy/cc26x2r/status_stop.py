from mat.ble.bluepy.cc26x2r_logger_controller import LoggerControllerCC26X2R
from _macs import get_mac


def stop():

    mac = get_mac()
    lc = LoggerControllerCC26X2R(mac)

    if lc.open():
        rv = lc.ble_cmd_stp()
        print('> stop: {}'.format(rv))
    else:
        print('{} connection error'.format(__name__))
    lc.close()


if __name__ == '__main__':
    stop()
