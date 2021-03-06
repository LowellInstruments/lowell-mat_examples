import time

from mat.ble.bluepy.cc26x2r_logger_controller import LoggerControllerCC26X2R


def send_con_command():

    mac = '60:77:71:22:C8:6F'
    lc = LoggerControllerCC26X2R(mac)

    if lc.open():
        rv = lc.ble_cmd_con()
        print('CON ->', rv)
        time.sleep(2)

    else:
        print('{} connection error'.format(__name__))
    lc.close()


if __name__ == '__main__':
    send_con_command()
