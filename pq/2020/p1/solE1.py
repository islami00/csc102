def points_sys(speed):
    if speed < 70:
        print("OK")
    else:
        demerit = (speed - 70) // 5
        if demerit > 12:
            print("License suspended")
        else:
            print("Points:", demerit)
