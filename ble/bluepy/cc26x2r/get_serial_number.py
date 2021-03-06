from mat.ble.bluepy.cc26x2r_logger_controller import LoggerControllerCC26X2R



def get_serial_number():

    mac = '60:77:71:22:CA:6D'
    lc = LoggerControllerCC26X2R(mac)

    if lc.open():
        rv = lc.ble_cmd_gsn()
        print('> get serial number: {}'.format(rv))
    else:
        print('{} connection error'.format(__name__))
    lc.close()


if __name__ == '__main__':
    get_serial_number()
