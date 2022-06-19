
from mat.ble.bluepy.cc26x2r_logger_controller import LoggerControllerCC26X2R

# V1 example
# {
# 	"project_name": "osu",
# 	"forget_time": 86400,
# 	"wifi": {
# 		"ssid": "wifi_ssid",
# 		"pass": "wifi_pass"
# 	},
# 	"ddp_ws": {
# 		"ip": "10.0.0.205",
# 		"port": 5000
# 	},
#     "logger_macs": {
#         "11:22:33:44:55:66": "fake",
#         "66:66:66:66:66:66": "moana"
#     }
# }


def file_pcs():

    mac = '60:77:71:22:CA:6D'
    lc = LoggerControllerCC26X2R(mac)

    if lc.open():
        rv = lc.ble_cmd_stp()
        print(rv)
        s = 'osu 86400 wifi_ssid wifi_pass 10.0.0.205 5000'
        rv = lc.ble_cmd_pcs(s)
        print('> DDP config cmd: {}'.format(rv))
    else:
        print('{} connection error'.format(__name__))
    lc.close()


if __name__ == '__main__':
    file_pcs()
