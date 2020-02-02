class Solution(object):
    def minMeetingRooms(self, intervals):
        
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if len(intervals) < 1:
            return 0
        
       
        
        #sort intervals by starting time
        intervals = sorted(intervals, key=lambda r: r[0])
        
        #create min heap for end time with the endtime of the first meeting
        heap = [intervals[0][1]]
        heapq.heapify(heap)
        total = 1
        occupied = 1
        
        #free room list
        freeRoom = list()
        
        # if the no free room then add the room
        # check freeroom
        for i, newMeeting in enumerate(intervals[1:]):
            newStartTime = newMeeting[0]
            oldEndTime = heap[0]
            # if start time of the new meeting is < endTime
            if newStartTime < oldEndTime:
                #create new meeting room and increment occupied
                total += 1
                occupied +=1
            else:
                #pop the available
                heapq.heappop(heap)
            #push new meeting endTime
            heapq.heappush(heap,newMeeting[1])
        
        return total