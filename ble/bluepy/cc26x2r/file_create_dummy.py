from mat.ble.bluepy.cc26x2r_logger_controller import LoggerControllerCC26X2R


def file_dummy():

    mac = '60:77:71:22:CA:6D'
    lc = LoggerControllerCC26X2R(mac)

    if lc.open():
        rv = lc.ble_cmd_stp()
        print(rv)
        rv = lc.ble_cmd_mts()
        print('> my tool set cmd: {}'.format(rv))
    else:
        print('{} connection error'.format(__name__))
    lc.close()


if __name__ == '__main__':
    file_dummy()
