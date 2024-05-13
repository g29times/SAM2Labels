# https://blog.51cto.com/forever8/6441245#
import schedule
import time
from streamlit import get

# TODO 未完成
def job(url):
    print("I'm working...")
    get.get_labels(url)

schedule.every().minute.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)