#!/usr/bin/env python

import datetime

class Record:
    def __init__(self, id, create_time, weight=1, some_str=None):
        self.id = id
        self.create_time = create_time
        self.weight = weight
        self.some_str = some_str

    def __repr__(self):
        return f'Record(id={self.id}, create_time={self.create_time}, weight={self.weight}, some_str={self.some_str})'

min_datetime = datetime.datetime(1970, 1, 1, 0, 0, 0)

records = []
records.append(Record(1, datetime.datetime(2022, 12, 20, 15, 45, 8)))
records.append(Record(2, datetime.datetime(2022, 12, 20, 13, 48, 9), 0, 'foo'))
records.append(Record(3, None, 10))
records.append(Record(4, None))
records.append(Record(5, datetime.datetime(2022, 12, 19, 13, 48, 9), 100, 'foo'))

def print_records():
    for record in records:
        print(record)

print('Before sorting:')
print_records()

records.sort(key=lambda x: (-x.weight, x.create_time if x.create_time else min_datetime))

print()
print('After sorting:')
print_records()

records.sort(key=lambda x: (1 if x.some_str else 0, -x.weight, x.create_time if x.create_time else min_datetime))

print()
print('After sorting:')
print_records()
