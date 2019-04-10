from apscheduler.schedulers.blocking import BlockingScheduler
from scrapper import movie_poller

sched = BlockingScheduler()

sched.add_job(movie_poller, 'cron', hour='1-23', minute='0,30')

print "Starting scheduler!"
sched.start()