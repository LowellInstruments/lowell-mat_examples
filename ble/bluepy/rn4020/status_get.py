
from mat.ble.bluepy.rn4020_logger_controller import LoggerControllerRN4020


def status():
    mac = '11:22:33:44:55:66'
    lc = LoggerControllerRN4020(mac)

    if lc.open():
        rv = lc.ble_cmd_sts()
        print('status', rv)
    else:
        print('{} connection error'.format(__name__))
    lc.close()


if __name__ == '__main__':
    status()
