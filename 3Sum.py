class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        # -2,-2,-2,-1,0,1,2
        #     ^
        #                 ^
        #  ^
        #make sure the anchor point is unique
        nums = sorted(nums)
        end = len(nums)
        res= list()   
        for i in range(0, end-2):
            val = nums[i]
            if i > 0 and val == nums[i-1]:
                continue
            mid = val
            left = i + 1
            right = end - 1
            #find the left and right that sum up to zero; given val
            while left < right:
                s = mid + nums[left] + nums[right]
                #if negative then we need bigger number
                if s < 0:
                    left += 1
                #we need to bring down our sum
                elif s > 0:
                    right -= 1
                #zero
                else:
                    res.append([val, nums[left], nums[right]])                    
                    #there could be more solution with val
                    # canno be end
                    while left + 1 < end and nums[left] == nums[left + 1]:
                        left += 1
                    while right - 1 >= 0 and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                    
        return res
                    
        