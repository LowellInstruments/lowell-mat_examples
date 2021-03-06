import time
from mat.crc import calculate_local_file_crc
from mat.ble.bluepy.cc26x2r_logger_controller import LoggerControllerCC26X2R
from pathlib import Path

from mat.data_converter import default_parameters, DataConverter


def flood():

    mac = '60:77:71:22:C9:B3'

    lc = LoggerControllerCC26X2R(mac)

    if lc.open():
        for i in range(100):
            rv = lc.ble_cmd_sts()
            print(rv)
    else:
        print('{} connection error'.format(__name__))
    lc.close()


if __name__ == '__main__':
    # test robustness of the firmware
    flood()
