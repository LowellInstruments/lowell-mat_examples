
from mat.ble.bluepy.cc26x2r_logger_controller import LoggerControllerCC26X2R


def file_config(c: dict):

    mac = '11:22:33:44:55:66'
    lc = LoggerControllerCC26X2R(mac)

    if lc.open():
        rv = lc.ble_cmd_cfg(c)
        print('> config cmd: {}'.format(rv))
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
    file_config(d)
