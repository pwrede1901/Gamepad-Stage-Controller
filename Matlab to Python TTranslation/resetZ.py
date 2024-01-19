from sendCMD import send_cmd
from AddErrorCode import add_error_code

def resetZ(obj1):
    success = 0

    # Execute alarm reset
    out1, num1 = send_cmd(obj1, add_error_code(':01050407FF00'), 1)

    # Restore normal status
    out2, num2 = send_cmd(obj1, add_error_code(':010504070000'), 1)

    print(out1)
    print(out2)

    return success
