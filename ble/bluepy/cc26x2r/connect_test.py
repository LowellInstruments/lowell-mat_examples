import time
from mat.ble.bluepy.cc26x2r_logger_controller import LoggerControllerCC26X2R
from _macs import get_mac


def connect():

    mac = get_mac()
    lc = LoggerControllerCC26X2R(mac)

    # ---------------------------
    # try to connect 1000 times
    # show success percentage
    # ---------------------------
    ok = 0
    for i in range(1, 1000):
        if lc.open():
            ok += 1
        lc.close()
        s = 'connection {} / {} = {}%'
        print(s.format(ok, i, 100 * (ok / i)))
        time.sleep(3)


if __name__ == '__main__':
    connect()
