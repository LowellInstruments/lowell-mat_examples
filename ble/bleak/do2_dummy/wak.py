from ble.bleak.do2.wak import wak
from mat.ble.bleak_beta.logger_do2_dummy import LoggerDO2Dummy


if __name__ == "__main__":
    wak(LoggerDO2Dummy)
