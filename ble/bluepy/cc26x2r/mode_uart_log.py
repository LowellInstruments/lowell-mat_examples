from mat.ble.bluepy.cc26x2r_logger_controller import LoggerControllerCC26X2R
from _macs import get_mac


def toggle_mode_uart():

    mac = get_mac()
    lc = LoggerControllerCC26X2R(mac)

    if lc.open():
        rv = lc.ble_cmd_log()
        print('> log enabled: {}'.format(rv))
    else:
        print('{} connection error'.format(__name__))
    lc.close()


if __name__ == '__main__':
    toggle_mode_uart()
