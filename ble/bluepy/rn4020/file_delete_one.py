from ble.bluepy.cc26x2r.file_delete_one import file_del
from mat.ble.bluepy.rn4020_logger_controller import LoggerControllerRN4020


if __name__ == '__main__':
    s = '2110407_T&P_(0).lid'
    file_del(s, cla=LoggerControllerRN4020)