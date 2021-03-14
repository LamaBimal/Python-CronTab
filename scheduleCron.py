import logging, sys
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
from crontab import CronTab
my_cron = CronTab(user='bimal')
for job in my_cron:
    print job # print available cron job
    my_cron.remove(job) # remove existing jobs
# Adding cron job

job = my_cron.new(command='/home/bimal/writeDate.py',comment='checker_cron1')
job.hour.every(1)
job.minute.every(59)
#job.enable(False)
job.enable()
list = my_cron.find_command('checker_cron')
for j in list:
    j.enable(False)
my_cron.write()
