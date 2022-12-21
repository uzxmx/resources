#!/usr/bin/env python

import datetime

class Record:
    def __init__(self, id, create_time):
        self.id = id
        self.create_time = create_time

    def __repr__(self):
        return f'Record(id={self.id}, create_time={self.create_time})'

min_datetime = datetime.datetime(1970, 1, 1, 0, 0, 0)

records = []
records.append(Record(1, datetime.datetime(2022, 12, 20, 15, 45, 8)))
records.append(Record(2, datetime.datetime(2022, 12, 20, 13, 48, 9)))
records.append(Record(3, None))
records.append(Record(4, None))
records.append(Record(5, datetime.datetime(2022, 12, 19, 13, 48, 9)))

def print_records():
    for record in records:
        print(record)

print('Before sorting:')
print_records()

records.sort(key=lambda x: x.create_time if x.create_time else min_datetime)

print()
print('After sorting:')
print_records()
