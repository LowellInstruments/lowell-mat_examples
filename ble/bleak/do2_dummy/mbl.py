from ble.bleak.do2.mbl import mbl
from mat.ble.bleak_beta.logger_do2_dummy import LoggerDO2Dummy


if __name__ == "__main__":
    mbl(LoggerDO2Dummy)
