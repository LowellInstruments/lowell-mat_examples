from mat.ble.bluepy.cc26x2r_logger_controller import LoggerControllerCC26X2R
from ble.bluepy.examples_utils import get_mac


def uptime(cla=LoggerControllerCC26X2R):

    mac = get_mac(cla)
    lc = cla(mac)

    if lc.open():
        rv = lc.ble_cmd_utm()
        print('> uptime: {} seconds'.format(rv))
    else:
        print('{} connection error'.format(__name__))
    lc.close()


if __name__ == '__main__':
    uptime()
