import ctypes

def DetectClick():
    bnum = 0x01
    state = 0
    cnt = 0
    while True:
        if ctypes.windll.user32.GetKeyState(bnum) not in [0, 1] and state == 0:
            cnt += 1
            state = 1
        elif ctypes.windll.user32.GetKeyState(bnum) in [0, 1] and state == 1:
            state = 0
        if ctypes.windll.user32.GetKeyState(37) not in [0, 1]:
            print('number of clicks =', cnt)
            break

DetectClick()
