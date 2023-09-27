# Jobrunr

```
exists job:backgroundjobservers:created
exists job:recurringjobs
get job:recurringjobs

keys job:*
keys job:jobdetails:SCHEDULED

type job:jobdetails:ENQUEUED
smembers job:jobdetails:ENQUEUED
smembers job:jobdetails:SCHEDULED
smembers job:jobdetails:FAILED
smembers job:jobdetails:PROCESSING

exists job:recurring-job-id:ENQUEUED

get recurringjobs

# zset
type queue:jobs:SCHEDULED

zcard queue:jobs:SCHEDULED
zrange queue:jobs:SCHEDULED 0 -1

# zet
type queue:scheduledjobs
zrange queue:scheduledjobs 0 -1
```
