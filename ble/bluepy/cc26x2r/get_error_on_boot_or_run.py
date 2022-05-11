from mat.ble.bluepy.cc26x2r_logger_controller import LoggerControllerCC26X2R



# todo > test this
def error_on_boot_or_run():

    mac = '11:22:33:44:55:66'
    lc = LoggerControllerCC26X2R(mac)

    if lc.open():
        rv = lc.ble_cmd_ebr()
        print('> get error on boot or run: {}'.format(rv))
    else:
        print('{} connection error'.format(__name__))
    lc.close()


if __name__ == '__main__':
    error_on_boot_or_run()
