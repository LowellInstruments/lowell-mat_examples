from ble.bleak.do2.sws import sws
from mat.ble.bleak_beta.logger_do2_dummy import LoggerDO2Dummy


if __name__ == "__main__":
    s = 'stop_at_lab.lid'
    sws(s, LoggerDO2Dummy)
