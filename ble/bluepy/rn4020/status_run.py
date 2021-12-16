from mat.ble.bluepy.rn4020_logger_controller import LoggerControllerRN4020
from ble.bluepy.cc26x2r.status_run import run


if __name__ == '__main__':
    run(cla=LoggerControllerRN4020)
