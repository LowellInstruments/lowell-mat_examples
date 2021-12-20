from ble.bleak.do2.siz import siz
from mat.ble.bleak_beta.logger_do2_dummy import LoggerDO2Dummy


if __name__ == "__main__":
    s = 'dummy_1631032845.lid'
    siz(s, LoggerDO2Dummy)
