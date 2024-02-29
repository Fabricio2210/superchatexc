import schedule
import time
from wrapper import wrapper
print(f"running superchatexcel!!")
schedule.every().day.at("18:15").do(lambda: wrapper("dsp","superchats"))
schedule.every().day.at("18:20").do(lambda: wrapper("reacts","superchats"))
schedule.every().day.at("18:25").do(lambda: wrapper("doody","superchats"))
schedule.every().day.at("18:30").do(lambda: wrapper("throwback","superchats"))
try:
    while True:
        time.sleep(1)
        schedule.run_pending()
except (KeyboardInterrupt, SystemExit):
    schedule.clear()