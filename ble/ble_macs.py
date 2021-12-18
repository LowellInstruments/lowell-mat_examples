from mat.ble.bleak_beta.logger_mat import LoggerMAT
from mat.ble.bluepy.cc26x2r_logger_controller import LoggerControllerCC26X2R
from mat.ble.bluepy.rn4020_logger_controller import LoggerControllerRN4020


MAC_LOGGER_DO2_0_SDI12 = '60:77:71:22:c8:18'
MAC_LOGGER_DO2_0_MODBUS = '04:EE:03:6C:EF:79'
MAC_LOGGER_DO2_1_MODBUS = '60:77:71:22:C9:EE'
MAC_LOGGER_MAT1_0 = '00:1e:c0:6c:76:13'
MAC_LOGGER_MAT1_1 = '00:1e:c0:6c:76:0b'
MAC_LOGGER_MAT1_2 = '00:1e:c0:3d:7a:f2'
MAC_MOANA_0051 = 'C9:3C:F8:37:E9:6A'
MAC_LOGGER_DO2_DUMMY = '11:22:33:44:55:D0'


def get_mac(cla, forced=''):
    if forced:
        return forced

    # -------
    # bluepy
    # -------
    if cla is LoggerControllerCC26X2R:
        return MAC_LOGGER_DO2_1_MODBUS
    if cla is LoggerControllerRN4020:
        return MAC_LOGGER_MAT1_1

    # -------
    # bleak
    # -------
    if cla is LoggerMAT:
        return MAC_LOGGER_MAT1_0

    print('class is {}'.format(cla))

