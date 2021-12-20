from ble.bleak.do2.whs import whs
from mat.ble.bleak_beta.logger_do2_dummy import LoggerDO2Dummy


if __name__ == "__main__":
    whs('TMO12345', LoggerDO2Dummy)
