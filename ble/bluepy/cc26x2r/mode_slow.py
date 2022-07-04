from mat.ble.bluepy.cc26x2r_logger_controller import LoggerControllerCC26X2R


def set_mode_slow(s):

    assert s in ('on', 'off')
    mac = '60:77:71:22:CA:6D'
    lc = LoggerControllerCC26X2R(mac)

    if lc.open():
        print('setting SLOW mode to {}'.format(s))
        lc.ble_cmd_slw_ensure(s)
    else:
        print('{} connection error'.format(__name__))
    lc.close()


if __name__ == '__main__':
    set_mode_slow('on')
