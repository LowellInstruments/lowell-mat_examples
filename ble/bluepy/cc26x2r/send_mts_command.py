from mat.ble.bluepy.cc26x2r_logger_controller import LoggerControllerCC26X2R


def send_mts_command():

    mac = '60:77:71:22:C8:6F'
    lc = LoggerControllerCC26X2R(mac)

    if lc.open():
        rv = lc.ble_cmd_stp()
        print('STP', rv)

        rv = lc.ble_cmd_mts()
        print('MTS', rv)

        rv = lc.ble_cmd_dir_ext('lid')
        print('list lid files: {}\n'.format(rv))

    else:
        print('{} connection error'.format(__name__))
    lc.close()


if __name__ == '__main__':
    send_mts_command()
