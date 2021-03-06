
from mat.ble.bluepy.rn4020_logger_controller import LoggerControllerRN4020


def get_time():
    mac = '11:22:33:44:55:66'
    lc = LoggerControllerRN4020(mac)

    if lc.open():
        rv = lc.ble_cmd_gtm()
        print('get time', rv)
    else:
        print('{} connection error'.format(__name__))
    lc.close()


if __name__ == '__main__':
    get_time()
