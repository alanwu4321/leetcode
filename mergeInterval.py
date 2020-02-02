class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        merged = list()
        
        
        intervals = sorted(intervals, key= lambda k: k[0])
        
        for i, itv in enumerate(intervals):
            #if merged is empty and no overlap
            if not merged or not merged[-1][1] >= itv[0]:
                merged.append(itv)
            else:
                #ONLY update if the new element endtime is bigger
                merged[-1][1] = max(itv[1], merged[-1][1])
        
        return merged