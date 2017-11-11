from collections import defaultdict
from datetime import datetime

import json

data = json.load([
    {
        "location": "NRT", 
        "temperature": 36, 
        "timestamp": "2012-06-14 13:09:00"
    }, 
    {
        "location": "NRT", 
        "temperature": 52, 
        "timestamp": "2012-06-14 13:15:00"
    },
])

#
buckets = defaultdict(lambda: defaultdict(list))

# buckets['NRT'][(2012, 6, 14, 13)].append(52)


#
for entry in data:
    location = data['location']
    timestamp = datetime.strptime('format', data['timestamp'])

    timestamp_key = (
        timestamp.year,
        timestamp.month,
        timestamp.day,
        timestamp.hour,
    )

    buckets[location][timestamp_key].append(data['temperature'])

def average(items):
    return sum(items) / len(items)

locations = sorted(buckets.keys())
for location in buckets.keys():
    location_data = buckets[location]
    timestamp_keys = sorted(location_data)
    for timestamp_key in timestamp_keys:
        print(location)
        print(timestamp_key)
        print(average(location_data[timestamp_key]))

