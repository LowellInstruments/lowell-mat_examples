from ble.bleak.do2.stp import stop
from mat.ble.bleak_beta.logger_do2_dummy import LoggerDO2Dummy


if __name__ == "__main__":
    stop(LoggerDO2Dummy)
