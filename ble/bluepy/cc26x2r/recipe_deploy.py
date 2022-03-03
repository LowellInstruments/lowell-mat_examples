from mat.ble.bluepy.cc26x2r_logger_controller import LoggerControllerCC26X2R
from _macs import get_mac


def deploy(c_d: dict, mac):

    lc = LoggerControllerCC26X2R(mac)

    if lc.open():
        rv = lc.ble_cmd_stp()
        print('> stop: {}'.format(rv))
        rv = lc.ble_cmd_stm()
        print('> set time: {}'.format(rv))
        rv = lc.ble_cmd_gtm()
        print('> get time: {}'.format(rv))
        rv = lc.ble_cmd_frm()
        print('> format: {}'.format(rv))
        rv = lc.ble_cmd_sts()
        print('> status: {}'.format(rv))
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


if __name__ == '__main__':
    cfg_do = {
        "DFN": "low",
        "TMP": 0, "PRS": 0,
        "DOS": 1, "DOP": 1, "DOT": 1,
        "TRI": 10, "ORI": 10, "DRI": 30,
        "PRR": 1,
        "PRN": 1,
        "STM": "2012-11-12 12:14:00",
        "ETM": "2030-11-12 12:14:20",
        "LED": 1
    }
    cfg_mat = {
        "DFN": "low",
        "TMP": 1, "PRS": 0,
        "DOS": 0, "DOP": 0, "DOT": 0,
        "TRI": 10, "ORI": 10, "DRI": 30,
        "PRR": 1,
        "PRN": 1,
        "STM": "2012-11-12 12:14:00",
        "ETM": "2030-11-12 12:14:20",
        "LED": 1
    }

    # d = cfg_do
    d = cfg_mat
    list_of_macs = [get_mac(), ]
    for each_mac in list_of_macs:
        deploy(d, each_mac)
