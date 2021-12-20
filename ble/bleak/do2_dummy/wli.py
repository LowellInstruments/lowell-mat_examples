from ble.bleak.do2.wli import wli
from mat.ble.bleak_beta.logger_do2_dummy import LoggerDO2Dummy


if __name__ == "__main__":
    wli('SN8888888', LoggerDO2Dummy)
