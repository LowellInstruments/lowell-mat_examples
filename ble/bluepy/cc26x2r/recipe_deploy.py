from mat.ble.bluepy.cc26x2r_logger_controller import LoggerControllerCC26X2R
from _macs import get_mac


def _deploy(c_d: dict, mac):

    lc = LoggerControllerCC26X2R(mac)

    if lc.open():
        rv = lc.ble_cmd_sts()
        print('> status: {}'.format(rv))
        rv = lc.ble_cmd_stp()
        print('> stop: {}'.format(rv))
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
        # rv = lc.ble_cmd_run()
        # print('> run: {}'.format(rv))

    else:
        print('{} connection error'.format(__name__))
    lc.close()


def cfg_do():
    # mac = get_mac()
    # mac = '60:77:71:22:C8:49'
    # mac = '04:ee:03:73:87:22'
    mac = '60:77:71:22:C8:6f'
    # mac = '04:EE:03:E2:4F:F9'
    # mac = '60:77:71:22:CA:18'
    # mac = '58:93:D8:A4:B6:35'
    # mac = '60:77:71:22:C9:cd'
    # mac = '60:77:71:22:CA:3A'

    d = {
        "DFN": "kaz",
        "TMP": 0, "PRS": 0,
        "DOS": 1, "DOP": 1, "DOT": 1,
        "TRI": 10, "ORI": 10, "DRI": 300,
        "PRR": 1,
        "PRN": 1,
        "STM": "2012-11-12 12:14:00",
        "ETM": "2030-11-12 12:14:20",
        "LED": 1
    }
    _deploy(d, mac)


def cfg_mat():
    mac = get_mac()

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

    cfg_do()
    # cfg_mat()
