

#!/bin/python3

import collections
import heapq
import math
import os
import random
import re
import sys


#
# Complete the 'droppedRequests' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY requestTime as parameter.
#

def isOverBroad(request, queue, limit):
    return len(queue) > 0 and request - queue[0] >= limit


def droppedRequests(requestTime):
    queue1Sec = list()
    queue10Sec = list()
    queue60Sec = list()
    count = 0
    for request in requestTime:
        for queue, limit in ((queue1Sec, 1), (queue10Sec, 10), (queue60Sec, 60)):
            while isOverBroad(request, queue, limit):
                queue.pop(0)

        to_drop = 0
        for queue, limit in ((queue1Sec, 3), (queue10Sec, 20), (queue60Sec, 60)):
            if len(queue) >= limit:
                to_drop = 1
                if queue:
                    queue.pop(0)
            queue.append(request)

        count += to_drop

    return count


if __name__ == '__main__':


print(droppedRequests([1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5,
                       5, 5, 6, 6, 6, 7, 7, 7, 7, 11, 11, 11, 11]))

print(droppedRequests([1, 1, 1, 1, 2, 2, 2, 3, 3,
                       3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7]))


print(droppedRequests([1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 9,
                       10, 10, 11, 11, 11, 11, 11, 11, 12, 12, 12, 12, 12, 12, 12, 13, 13, 13, 13, 14, 14, 14, 14, 14, 16, 16, 16, 16, 16,
                       16, 17, 17, 17, 18, 18, 18, 18, 18, 18, 18, 18, 19, 19, 19, 19, 19, 19, 19, 20, 20, 20, 20, 20]))


#!/bin/python3

#
# Complete the 'maximumTeamQuality' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY speed
#  2. INTEGER_ARRAY professionalism
#  3. INTEGER maxDashers
#

#!/bin/python3


#
# Complete the 'maximumTeamQuality' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY speed
#  2. INTEGER_ARRAY professionalism
#  3. INTEGER maxDashers
#


def maximumTeamQuality(speed, professionalism, maxDashers):
    n = len(speed)
    pairs = list()
    for i in range(n):
        pairs.append((speed[i], professionalism[i]))

    # sort by professionalism
    pairs = sorted(pairs, key=lambda p: p[1])
    pairs.reverse()

    max_ = 0
    total = 0

    pq = list()
    heapq.heapify(pq)

    # loop from largest profession to least and keep track of max speed
    for i in range(n):
        # use the current one and the ones before
        speed, prof = pairs[i]
        heapq.heappush(pq, speed)
        total += speed
        if len(pq) > maxDashers:
            # get rid of the min speed that we have seen to ensure max total speed
            total -= heapq.heappop(pq)

        max_ = max(max_, total * prof)

    return max_


