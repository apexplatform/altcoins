from crontab import CronTab

cron = CronTab(user='huazhao')
job = cron.new(command='python3 /Users/huazhao/altcoins/collectaltcoinData.py')
job.minute.every(1)

cron.write()
