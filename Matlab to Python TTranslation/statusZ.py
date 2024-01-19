from sendCMD import send_cmd
from AddErrorCode import add_error_code
from hex2bin import hex2bin


def statusZ(obj1):
    # Create status report 2 (page 41)
    out, num = send_cmd(obj1, add_error_code(':010390070001'), 0)
    status = hex2bin(out[6:10])

    print('Emergency stop status:', status[0])

    return status[0]
