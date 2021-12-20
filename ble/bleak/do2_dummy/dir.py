from ble.bleak.do2.dir import list_files
from mat.ble.bleak_beta.logger_do2_dummy import LoggerDO2Dummy


if __name__ == "__main__":
    list_files(LoggerDO2Dummy)
