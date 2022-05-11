from mat.ble.bluepy.cc26x2r_logger_controller import LoggerControllerCC26X2R



def toggle_mode_uart():

    mac = '11:22:33:44:55:66'
    lc = LoggerControllerCC26X2R(mac)

    if lc.open():
        rv = lc.ble_cmd_log()
        print('> log enabled: {}'.format(rv))
    else:
        print('{} connection error'.format(__name__))
    lc.close()


if __name__ == '__main__':
    toggle_mode_uart()
