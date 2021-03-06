from mat.ble.bluepy.cc26x2r_logger_controller import LoggerControllerCC26X2R



def file_get_name():

    mac = '11:22:33:44:55:66'
    lc = LoggerControllerCC26X2R(mac)

    if lc.open():
        rv = lc.ble_cmd_rfn()
        print('> get data file name: {}'.format(rv))
    else:
        print('{} connection error'.format(__name__))
    lc.close()


if __name__ == '__main__':
    file_get_name()
