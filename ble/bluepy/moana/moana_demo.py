import os
import time
from pathlib import Path
from mat.ble.bluepy.moana_logger_controller import LoggerControllerMoana


mac = '11:22:33:44:55:66'


def download_moana_logger(fol):

    # -----------------------------
    # open BLE connection
    # -----------------------------
    print('reaching moana {}...'.format(mac))
    lc = LoggerControllerMoana(mac)
    if not lc.open():
        print('connection error')
        return

    # -----------------------------
    # authenticate to moana logger
    # -----------------------------
    lc.auth()

    # ------------------------------
    # download file in moana logger
    # ------------------------------
    name_csv_moana = lc.file_info()
    print('downloading file {}...'.format(name_csv_moana))
    data = lc.file_get()

    # ------------------------------
    # save and convert file
    # ------------------------------
    name_bin_local = lc.file_save(fol, data)
    if name_bin_local:
        print('saved as {}'.format(name_bin_local))
        name_csv_local = lc.file_cnv(name_bin_local, fol, len(data))
        if name_csv_local:
            p = '{}/{}'.format(fol, name_csv_local)
            print('converted files -> {}*'.format(p))
        else:
            print('conversion error')

    # ------------------------------
    # ensure logger has our time
    # ------------------------------
    lc.time_sync()
    time.sleep(1)

    # ----------------------------------------------------------
    # doing file_clear() re-deploys logger
    # for development, comment it to do repeated download tests
    # ----------------------------------------------------------
    # if not lc.file_clear():
    #    print('error file_clear')

    lc.close()


if __name__ == '__main__':

    # prepare local download folder
    files_fol = str(Path.home()) + '/Downloads/moana_demo'
    try:
        os.mkdir(files_fol)
    except OSError as error:
        pass

    download_moana_logger(files_fol)
