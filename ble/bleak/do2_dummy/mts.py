from ble.bleak.do2.mts import create_fake_file
from mat.ble.bleak_beta.logger_do2_dummy import LoggerDO2Dummy


if __name__ == "__main__":
    create_fake_file(LoggerDO2Dummy)
