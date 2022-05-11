import time
from mat.ble.bluepy.cc26x2r_logger_controller import LoggerControllerCC26X2R


def connect():

    mac = '60:77:71:22:Ca:6d'
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
