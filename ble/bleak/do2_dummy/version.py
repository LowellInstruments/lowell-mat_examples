from ble.bleak.do2.version import get_version
from mat.ble.bleak_beta.logger_do2_dummy import LoggerDO2Dummy


if __name__ == "__main__":
    get_version(LoggerDO2Dummy)
