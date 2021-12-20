from ble.bleak.do2.delete_file import delete_file
from mat.ble.bleak_beta.logger_do2_dummy import LoggerDO2Dummy


if __name__ == "__main__":
    s = 'dummy_1631024616.lid'
    delete_file(s, LoggerDO2Dummy)
