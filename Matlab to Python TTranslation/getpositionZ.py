from sendCMD import send_cmd
from AddErrorCode import add_error_code

def get_position_z(obj1):
    out, num = send_cmd(obj1, add_error_code(':010390000002'), True)

    n_bytes = int(out[5:7], 16)  # number of bytes encoding the position
    position = int(out[7:7 + 2 * n_bytes], 16)  # position in 1:100 mm
    position = position / 100  # position in mm

    return position
