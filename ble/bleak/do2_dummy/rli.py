from ble.bleak.do2.rli import rli
from mat.ble.bleak_beta.logger_do2_dummy import LoggerDO2Dummy


if __name__ == "__main__":
    rli(LoggerDO2Dummy)
