
# This is just a simple shared plaintext pad, with no execution capabilities.

# When you know what language you'd like to use for your interview,
# simply choose it from the dropdown in the top bar.

# You can also change the default language your pads are created with
# in your account settings: https://coderpad.io/settings

# Enjoy your interview!



# Your previous Python 3 content is preserved below:

# # 
# # Your previous Plain Text content is preserved below:
# # 
# # Given a list of events as (start_time, end_time) pairs, find the time range with the largest number of overlapping events.
# # 
# # 
# # 0        1.6        2.31     3.5       4.12     5.7
# # |---------|---------|--------|---------|--------|          <-  TIME RANGE
# #           |                  |
# # <------------------->                                             (0, 2.32)
# #           |                  |
# #           <---------------------------->                          (2.32, 4.12)
# #           |                  |
# #           |                  <------------------>                 (3.5, 5.7)
# #           |                  |
# # 
# # In the above drawing, we have three events. The time range between 1 and 3 (delimited by lines) has 3 overlapping events.
# # 
# # Example from drawing:           
# # Input: [(0, 3), (1, 4), (0, 4)] N
# # Output: (1, 3)
# # 
# # 


# timeDict = dict()
# maxTime = 0

# allTime = list()

# for i, meeting in enumerate(input):
#   allTime.append(meeting.start, meeting.end)
  

# sorted(allTime).removeDuplicate()

# for i, meeting in enumerate(input):
#   for i in range(allTime.indexOf(meeting.start), allTime.indexOf(meeting.end)):
#     if timeDict[allTime[i]] != None:
#       timeDict[allTime[i]]++
#     else:
#       timeDict[allTime[i]] = 1
#      maxTime = max(maxTime, timeDict[allTime[i]])
    
# temp = []
# for i, val in enumerate(allTime):
#   if timeDict[val] == maxTime:
#     temp.push(val)
#     if i < len(allTime)-1 && timeDict[allTime[i+1]] != maxTime:
#       break

# result = {start: temp[0], end: temp[len(temp)-1]}




def findFirstLast(arr, target):
  start, end = -1, -1
  for i, val in enumerate(arr):
    if start == -1 and val == target:
      start = i
    if val == target and i+1 < len(arr) and arr[i+1] != target:
      end = i
  return (start,end)

print(findFirstLast([1,1,3,4,4,4,5], 1))