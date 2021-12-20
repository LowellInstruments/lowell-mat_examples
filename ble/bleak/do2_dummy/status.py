from ble.bleak.do2.status import status
from mat.ble.bleak_beta.logger_do2_dummy import LoggerDO2Dummy


if __name__ == "__main__":
    status(LoggerDO2Dummy)
