from mat.ble.bluepy.cc26x2r_logger_controller import LoggerControllerCC26X2R


def set_info():

    mac = '60:77:71:22:CA:6D'
    lc = LoggerControllerCC26X2R(mac)

    if lc.open():
        rv = lc.ble_cmd_wli("SN1234567")
        print('> set info SN: {}'.format(rv))
    else:
        print('{} connection error'.format(__name__))
    lc.close()


if __name__ == '__main__':
    set_info()
