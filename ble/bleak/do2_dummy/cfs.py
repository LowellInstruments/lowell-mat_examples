from ble.bleak.do2.cfs import cfs
from mat.ble.bleak_beta.logger_do2_dummy import LoggerDO2Dummy

if __name__ == "__main__":
    cfs(LoggerDO2Dummy)
