from ble.bleak.do2.stm import set_time
from mat.ble.bleak_beta.logger_do2_dummy import LoggerDO2Dummy


if __name__ == "__main__":
    set_time(LoggerDO2Dummy)
