import schedule
import time
from wrapper import wrapper
print(f"running")
schedule.every().day.at("18:00").do(lambda: wrapper("dsp","superchats"))
schedule.every().day.at("18:10").do(lambda: wrapper("doody","superchats"))
try:
    while True:
        time.sleep(1)
        schedule.run_pending()
except (KeyboardInterrupt, SystemExit):
    schedule.clear()