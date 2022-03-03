# MAC_LOGGER_RN4020 = '00:1e:c0:6c:76:13'
# MAC_LOGGER_RN4020 = '00:1e:c0:6c:76:0b'
MAC_LOGGER_RN4020 = '00:1e:c0:3d:7a:f2'


def get_mac(forced=''):
    if forced:
        return forced
    return MAC_LOGGER_RN4020
