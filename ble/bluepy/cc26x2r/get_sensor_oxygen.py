import time
from mat.ble.bluepy.cc26x2r_logger_controller import LoggerControllerCC26X2R
from _macs import get_mac


def measure_oxygen(pre_stp=False):

    mac = get_mac()
    lc = LoggerControllerCC26X2R(mac)

    if lc.open():
        for i in range(1):

            if pre_stp:
                rv = lc.ble_cmd_stp()
                print('stop', rv)

            rv = lc.ble_cmd_gdo()
            print('> DO saturation:  {}.{} mg/l'.format(rv[0][:2], rv[0][2:]))
            print('> DO percentage:  {}.{} %'.format(rv[1][:2], rv[1][2:]))
            print('> DO temperature: {}.{} C'.format(rv[2][:2], rv[2][2:]))
            print('\n')
            time.sleep(5)
    else:
        print('{} connection error'.format(__name__))
    lc.close()


if __name__ == '__main__':
    measure_oxygen(pre_stp=True)
