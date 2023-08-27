import time

def focus_timer(minutes):
    seconds = minutes * 60
    print(f"开始专注倒计时，共计 {minutes} 分钟")

    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer_display = f'{mins:02d}:{secs:02d}'
        print(timer_display, end='\r')
        time.sleep(1)
        seconds -= 1

    print("专注时间结束！")
