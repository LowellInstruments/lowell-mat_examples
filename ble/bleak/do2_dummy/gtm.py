from ble.bleak.do2.gtm import get_time
from mat.ble.bleak_beta.logger_do2_dummy import LoggerDO2Dummy


if __name__ == "__main__":
    get_time(LoggerDO2Dummy)
