from ble.bleak.do2.slw import slow
from mat.ble.bleak_beta.logger_do2_dummy import LoggerDO2Dummy


if __name__ == "__main__":
    slow(LoggerDO2Dummy)
