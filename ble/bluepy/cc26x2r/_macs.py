MAC_LOGGER_DO2_0_SDI12 = '60:77:71:22:c8:18'
MAC_LOGGER_DO2_0_MODBUS = '04:EE:03:6C:EF:30'


def get_mac(forced=''):
    if forced:
        return forced

    # return MAC_LOGGER_DO2_1_MODBUS
    return MAC_LOGGER_DO2_0_MODBUS

