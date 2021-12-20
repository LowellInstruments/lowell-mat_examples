from ble.bleak.do2.led import leds
from mat.ble.bleak_beta.logger_do2_dummy import LoggerDO2Dummy


if __name__ == "__main__":
    leds(LoggerDO2Dummy)
