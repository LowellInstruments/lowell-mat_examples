from mat.ble.bluepy.cc26x2r_logger_controller import LoggerControllerCC26X2R
from _macs import get_mac


def set_info():

    mac = get_mac()
    lc = LoggerControllerCC26X2R(mac)

    if lc.open():
        rv = lc.ble_cmd_wli("SN1234567")
        print('> set info SN: {}'.format(rv))
        rv = lc.ble_cmd_wli("CA1234")
        print('> set info CA: {}'.format(rv))
        rv = lc.ble_cmd_wli("BA5678")
        print('> set info BA: {}'.format(rv))
        rv = lc.ble_cmd_wli("MA1234ABC")
        print('> set info MA: {}'.format(rv))
    else:
        print('{} connection error'.format(__name__))
    lc.close()


if __name__ == '__main__':
    set_info()
