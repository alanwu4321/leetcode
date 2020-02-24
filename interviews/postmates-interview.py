# # delivery ID | timestamp(unix) | kind
# # ------------------------
# # 1 | 8/15/17 1:30pm | pickup
# # 1 | 8/15/17 2:00pm | dropoff
# # 2 | 8/15/17 2:30pm | pickup
# # 2 | 8/15/17 2:35pm | dropoff
# # 3 | 8/15/17 3:00pm | pickup
# # 3 | 8/15/17 3:10pm | dropoff

# # Pickup(1) --30min-- Dropoff(1) --X 30min X-- Pickup(2) --5min-- Pickup(3) --25min-- Dropoff(2) --10min-- Dropoff(3)

input = [
    (1, 1502803800, "pickup"),
    (2, 1502805600, "pickup"),
    (2, 1502807400, "dropoff"), 
    (3, 1502807700, "pickup"),  
    (3, 1502809200, "dropoff"), 
    (1, 1502809800, "dropoff"), 
]
def isPickUp(activity):
    return activity[2] == "pickup"

def getTime(activity):
    return activity[1]

def get_active_time(input):
    #empty input
    if not input:
        return -1

    pickUpTime = totalActiveTime = packageOnHand = 0

    for activity in input:
        if isPickUp(activity):
            packageOnHand += 1
            #first pick up
            if packageOnHand == 1:
                pickUpTime = getTime(activity)
        else:
            packageOnHand -= 1
            if packageOnHand == 0:
                totalActiveTime += getTime(activity) - pickUpTime
        
    return totalActiveTime

import datetime

# print(get_active_time(input)//60)
"""
  monday: 10am -> 4pm
  tuesday: 10am -> 4pm
  wednesday: 11am -> 8pm
  thursday: 11am -> 8pm
  friday: 11am -> 2am
  saturday: 5pm -> 4am
"""

#starting from 12am +  600 //60 => 10am

input = {
  "hours": [
    {
      "days": [1,2],
      "hours": {"start_min": 600, "end_min": 960}
    },
    {
      "days": [3,4],
      "hours": {"start_min": 660, "end_min": 1200}
    },
    {
      "days": [5],
      "hours": {"start_min": 660, "end_min": 120}
    },
    {
      "days": [6],
      "hours": {"start_min": 1020, "end_min": 240}
    }
  ]
}

def is_store_open(example, dt):
    dayOfWeek = _day_of_week(dt)
    minSinceMidnight = _minutes_since_midnight(dt)

    hmap = dict()
    for weekDays in example["hours"]:
        for weekDay in weekDays["days"]:
            hmap[weekDay] = [weekDays["hours"]]

    # firday endtime is 11am - 12am
    hmap[5][0]['end_min'] = 1440
    #saturday: 12am -> 2am, 5pm -> 12am
    hmap[6][0]['end_min'] = 1440
    hmap[6].append({"start_min": 0, "end_min": 120})
    #Sunday 12am -> 4am
    hmap[7] = [{"start_min": 0, "end_min": 240}]

    openHours = hmap[dayOfWeek]
    for openHour in openHours:
        if openHour['start_min'] <= minSinceMidnight <= openHour['end_min']:
            return True
    
    return False

# Helper functions

def _minutes_since_midnight(dt):
    midnight = datetime.datetime.combine(dt.date(), datetime.time())
    return (dt - midnight).seconds / 60

def _day_of_week(dt):
    "Return day of the week, where Monday = 1 ... Sunday == 7."
    return dt.isoweekday()

print(is_store_open(input, datetime.datetime(2020, 2, 22, 3, 0, 0)))