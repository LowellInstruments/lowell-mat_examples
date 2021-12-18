from mat.ble.bluepy.cc26x2r_logger_controller import LoggerControllerCC26X2R
from ble.ble_macs import get_mac


def reset(cla=LoggerControllerCC26X2R):

    mac = get_mac(cla)
    lc = cla(mac)

    if lc.open():
        rv = lc.ble_cmd_rst()
        print('> reset: {}'.format(rv))
    else:
        print('{} connection error'.format(__name__))
    lc.close()


if __name__ == '__main__':
    reset()

