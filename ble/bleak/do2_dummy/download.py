from ble.bleak.do2.download import download
from mat.ble.bleak_beta.logger_do2_dummy import LoggerDO2Dummy


if __name__ == "__main__":
    name = 'dummy_4151.lid'
    size = 4151
    download(name, size, LoggerDO2Dummy)

