from mat.ble.bluepy.cc26x2r_logger_controller import LoggerControllerCC26X2R



def run():

    # mac = '11:22:33:44:55:66'
    mac = '60:77:71:22:C8:6f'
    lc = LoggerControllerCC26X2R(mac)

    if lc.open():
        rv = lc.ble_cmd_run()
        print('> run: {}'.format(rv))
    else:
        print('{} connection error'.format(__name__))
    lc.close()


if __name__ == '__main__':
    run()
