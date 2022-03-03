import time
from mat.ble.bluepy.cc26x2r_logger_controller import LoggerControllerCC26X2R
from _macs import get_mac


def measure_oxygen():

    mac = get_mac()
    lc = LoggerControllerCC26X2R(mac)

    if lc.open():
        while 1:
            rv = lc.ble_cmd_gdo()
            print('> DO saturation:  {}.{} mg/l'.format(rv[0][:2], rv[0][2:]))
            print('> DO percentage:  {}.{} %'.format(rv[1][:2], rv[1][2:]))
            print('> DO temperature: {}.{} C'.format(rv[2][:2], rv[2][2:]))
            print('\n')
            time.sleep(10)
    else:
        print('{} connection error'.format(__name__))
    lc.close()


if __name__ == '__main__':
    measure_oxygen()
