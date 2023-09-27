#!/usr/bin/env python
"""
Demonstrates how to use the background scheduler to schedule a job that executes on 3 second
intervals.
"""

from datetime import datetime
import time
import os

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger


def tick():
    print('Tick! The time is: %s' % datetime.now())
    time.sleep(7)
    print('Finished %s' % datetime.now())


if __name__ == '__main__':
    scheduler = BackgroundScheduler({'apscheduler.job_defaults.max_instances': 5})
    seconds = []
    start = 0
    while start < 60:
        seconds.append(str(start))
        start += 5

    # scheduler.add_job(tick, 'cron',  CronTrigger.from_crontab('%s * * * *' % ','.join(seconds)))
    scheduler.add_job(tick, 'cron',  second=','.join(seconds))
    # scheduler.add_job(tick, 'interval', seconds=3)
    scheduler.start()
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        # This is here to simulate application activity (which keeps the main thread alive).
        while True:
            time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        # Not strictly necessary if daemonic mode is enabled but should be done if possible
        scheduler.shutdown()
