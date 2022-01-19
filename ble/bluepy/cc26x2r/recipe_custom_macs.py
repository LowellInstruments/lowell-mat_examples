from mat.ble.bluepy.cc26x2r_logger_controller import LoggerControllerCC26X2R


def _custom_deploy(mac, cla=LoggerControllerCC26X2R):

    lc = cla(mac)

    c_d = {
        "DFN": "low",
        "TMP": 0, "PRS": 0,
        "DOS": 1, "DOP": 1, "DOT": 1,
        "TRI": 10, "ORI": 10, "DRI": 60,
        "PRR": 1,
        "PRN": 1,
        "STM": "2012-11-12 12:14:00",
        "ETM": "2030-11-12 12:14:20",
        "LED": 1
    }

    if lc.open():
        print('\n logger mac', mac)

        rv = lc.ble_cmd_stp()
        print('> stop: {}'.format(rv))
        rv = lc.ble_cmd_gdo()
        print('> gdo: {}'.format(rv))
        rv = lc.ble_cmd_stm()
        print('> stm: {}'.format(rv))
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


def _custom_list_files(i, cla=LoggerControllerCC26X2R):

    mac = i
    lc = cla(mac)

    if lc.open():
        print('\n logger mac', mac)
        rv = lc.ble_cmd_stp()
        print('> stop: {}'.format(rv))
        rv = lc.ble_cmd_gtm()
        print('> gtm: {}'.format(rv))
        rv = lc.ble_cmd_gdo()
        print('> gdo: {}'.format(rv))
        rv = lc.ble_cmd_dir()
        print('> dir: {}'.format(rv))

    else:
        print('{} connection error'.format(__name__))
    lc.close()


if __name__ == '__main__':

    macs = (
        #'04:EE:03:73:88:1D',
        #'04:EE:03:73:87:22',
        #'60:77:71:22:c8:6f',
        #'60:77:71:22:ca:22',
        '58:93:D8:A4:B6:15',
    )

    for each_mac in macs:
        _custom_deploy(each_mac)
        # _custom_list_files(each_mac)
