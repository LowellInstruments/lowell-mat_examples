import time

from ble.ble_macs import get_mac
from mat.crc import calculate_local_file_crc
from mat.data_converter import default_parameters, DataConverter
from mat.ble.bluepy.cc26x2r_logger_controller import LoggerControllerCC26X2R
from pathlib import Path


def file_convert(path):
    try:
        assert path.endswith('.lid')
        print('\t\tConverting: {} --> '.format(path), end='')
        parameters = default_parameters()
        converter = DataConverter(path, parameters)
        converter.convert()
        return True
    except Exception as ex:
        print(ex)


def file_dwg(file_name, file_size: int, cla=LoggerControllerCC26X2R, forced_mac=''):

    mac = get_mac(cla) if not forced_mac else forced_mac
    lc = cla(mac)

    if not lc.open():
        print('{} connection error'.format(__name__))
        return

    rv = lc.ble_cmd_stp()
    print('STOP {}'.format(rv))

    # set the mobile level
    lc.ble_cmd_mbl_ensure('0')

    print('downloading', file_name, '...')
    rv = lc.ble_cmd_dwg(file_name)
    print('DWG {}'.format(rv))

    start = time.time()
    rv = lc.ble_cmd_dwl(file_size)
    path = str(Path.home() / 'Downloads' / file_name)
    end = time.time()

    if not rv:
        print('DWL error')

    else:
        speed = (file_size / (end - start))
        print('speed {} KBps'.format(speed))

        with open(path, 'wb') as f:
            f.write(rv)
            print('file downloaded to {}'.format(path))
        local_crc = calculate_local_file_crc(path)

        remote_crc = lc.ble_cmd_crc(file_name)
        rv = local_crc.lower() == remote_crc
        print('CRC check == {}'.format(rv))

        rv = file_convert(path)
        print('conversion == {}'.format(rv))
        if not rv:
            print('OK if dummy file')

    lc.close()


if __name__ == '__main__':

    file_dwg('1234567_low_20220127_115237.lid', 2178)
