from mat.ble.bluepy.cc26x2r_logger_controller import LoggerControllerCC26X2R



def file_del(s: str):

    mac = '11:22:33:44:55:66'
    lc = LoggerControllerCC26X2R(mac)

    if lc.open():
        rv = lc.ble_cmd_del(s)
        print('file delete one: {}'.format(rv))
    else:
        print('{} connection error'.format(__name__))
    lc.close()


if __name__ == '__main__':
    file_del('dummy_32.lid')
