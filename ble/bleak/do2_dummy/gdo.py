from ble.bleak.do2.gdo import gdo
from mat.ble.bleak_beta.logger_do2_dummy import LoggerDO2Dummy


if __name__ == "__main__":
    gdo(LoggerDO2Dummy)
