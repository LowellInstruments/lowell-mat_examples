from mat.ble.bluepy.cc26x2r_logger_controller import LoggerControllerCC26X2R



def file_size(s: str):

    mac = '11:22:33:44:55:66'
    lc = LoggerControllerCC26X2R(mac)

    if lc.open():
        rv = lc.ble_cmd_siz(s)
        print('> get one file size: {}'.format(rv))
    else:
        print('{} connection error'.format(__name__))
    lc.close()


if __name__ == '__main__':
    f = 'dummy_23.lid'
    file_size(f)
