from apscheduler.schedulers.blocking import BlockingScheduler
from scrapper import movie_poller

sched = BlockingScheduler()

sched.add_job(movie_poller, 'cron', hour='1-23', minute='0,10,20,30,40,50')

print("Starting scheduler! Will poll every half n hour.")
sched.start()