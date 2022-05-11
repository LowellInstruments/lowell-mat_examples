import time
from mat.crc import calculate_local_file_crc
from mat.ble.bluepy.cc26x2r_logger_controller import LoggerControllerCC26X2R
from pathlib import Path

from mat.data_converter import default_parameters, DataConverter


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


def file_dwg(file_name, file_size: int):

    mac = '60:77:71:22:C9:B3'

    lc = LoggerControllerCC26X2R(mac)

    if not lc.open():
        print('{} connection error'.format(__name__))
        return

    rv = False
    for i in range(3):
        rv = lc.ble_cmd_stp()
        print('STOP {}'.format(rv))
        if rv:
            break
        time.sleep(3)

    if not rv:
        print('could not stop logger')
        lc.close()
        return

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
        print('speed {} KBps'.format(speed / 1000))

        with open(path, 'wb') as f:
            f.write(rv)
            print('file downloaded to {}'.format(path))
        local_crc = calculate_local_file_crc(path)

        remote_crc = lc.ble_cmd_crc(file_name)
        rv = local_crc.lower() == remote_crc
        print(local_crc.lower(), remote_crc)
        print('CRC check == {}'.format(rv))

        rv = file_convert(path)
        print('conversion == {}'.format(rv))
        if not rv:
            print('OK if dummy file')

    lc.close()


if __name__ == '__main__':

    file_dwg('dummy_58.lid', 167936)
