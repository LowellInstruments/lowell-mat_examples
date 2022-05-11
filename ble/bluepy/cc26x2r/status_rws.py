from mat.ble.bluepy.cc26x2r_logger_controller import LoggerControllerCC26X2R



def rws():

    mac = '11:22:33:44:55:66'
    lc = LoggerControllerCC26X2R(mac)

    if lc.open():
        s = 'hello'
        rv = lc.ble_cmd_rws(s)
        print('> run: {}'.format(rv))
    else:
        print('{} connection error'.format(__name__))
    lc.close()


if __name__ == '__main__':
    rws()
