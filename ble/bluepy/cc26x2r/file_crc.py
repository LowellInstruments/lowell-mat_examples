from mat.ble.bluepy.cc26x2r_logger_controller import LoggerControllerCC26X2R



def file_crc(s: str):

    mac = '11:22:33:44:55:66'
    lc = LoggerControllerCC26X2R(mac)

    if lc.open():
        rv = lc.ble_cmd_crc(s)
        print('file remote crc: {}'.format(rv))
    else:
        print('{} connection error'.format(__name__))
    lc.close()


if __name__ == '__main__':
    # 1E8C58BC file contents '1234567890 abcdef!!"
    # aeef2a50 file contents 'abcdefgh'
    file_crc('MAT.cfg')
