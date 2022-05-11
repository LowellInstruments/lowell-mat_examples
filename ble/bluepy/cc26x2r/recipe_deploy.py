from mat.ble.bluepy.cc26x2r_logger_controller import LoggerControllerCC26X2R



def _deploy(c_d: dict, mac):

    lc = LoggerControllerCC26X2R(mac)

    if lc.open():
        rv = lc.ble_cmd_sts()
        print('> status: {}'.format(rv))
        rv = lc.ble_cmd_stp()
        print('> stop: {}'.format(rv))
        rv = lc.ble_cmd_gfv()
        print('> version: {}'.format(rv))
        rv = lc.ble_cmd_stm()
        print('> set time: {}'.format(rv))
        rv = lc.ble_cmd_gtm()
        print('> get time: {}'.format(rv))
        rv = lc.ble_cmd_gdo()
        print('> oxygen: {}'.format(rv))
        rv = lc.ble_cmd_frm()
        print('> format: {}'.format(rv))
        rv = lc.ble_cmd_wli("SN1234567")
        print('> set info SN: {}'.format(rv))
        rv = lc.ble_cmd_wli("CA1234")
        print('> set info CA: {}'.format(rv))
        rv = lc.ble_cmd_wli("BA5678")
        print('> set info BA: {}'.format(rv))
        rv = lc.ble_cmd_wli("MA1234ABC")
        print('> set info MA: {}'.format(rv))
        rv = lc.ble_cmd_cfg(c_d)
        print('> config cmd: {}'.format(rv))
        rv = lc.ble_cmd_run()
        print('> run: {}'.format(rv))

    else:
        print('{} connection error'.format(__name__))
    lc.close()


def cfg_do1():
    mac = '60:77:71:22:C8:6f'
    #mac = '58:93:d8:a4:b6:15'

    d = {
        "DFN": "kaz",
        "TMP": 0, "PRS": 0,
        "DOS": 1, "DOP": 1, "DOT": 1,
        "TRI": 10, "ORI": 10, "DRI": 30,
        "PRR": 1,
        "PRN": 1,
        "STM": "2012-11-12 12:14:00",
        "ETM": "2030-11-12 12:14:20",
        "LED": 1
    }
    _deploy(d, mac)


def cfg_do2():
    # mac = '60:77:71:22:CA:6A'
    mac = '60:77:71:22:C9:B3'

    d = {
        "DFN": "kaz",
        "TMP": 0, "PRS": 0,
        "DOS": 1, "DOP": 1, "DOT": 1,
        "TRI": 10, "ORI": 10, "DRI": 30,
        "PRR": 1,
        "PRN": 1,
        "STM": "2012-11-12 12:14:00",
        "ETM": "2030-11-12 12:14:20",
        "LED": 1
    }
    _deploy(d, mac)


def cfg_mat():
    mac = '11:22:33:44:55:66'

    d = {
        "DFN": "low",
        "TMP": 1, "PRS": 0,
        "DOS": 0, "DOP": 0, "DOT": 0,
        "TRI": 10, "ORI": 10, "DRI": 0,
        "PRR": 1,
        "PRN": 1,
        "STM": "2012-11-12 12:14:00",
        "ETM": "2030-11-12 12:14:20",
        "LED": 1
    }
    _deploy(d, mac)


if __name__ == '__main__':

    # cfg_do1()
    # cfg_mat()
    cfg_do2()

