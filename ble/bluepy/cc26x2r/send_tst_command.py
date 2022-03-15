from mat.ble.bluepy.cc26x2r_logger_controller import LoggerControllerCC26X2R


def send_tst_command():

    mac = '60:77:71:22:C8:49'
    lc = LoggerControllerCC26X2R(mac)

    if lc.open():
        rv = lc.ble_cmd_tst()
        print('TST', rv)
    else:
        print('{} connection error'.format(__name__))
    lc.close()


if __name__ == '__main__':
    send_tst_command()
