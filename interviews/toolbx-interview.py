#min jump to reach the end of the array

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [float('inf') for i in range(len(nums))]
        dp[0] = 0
        for ind, val in enumerate(nums):
            for jump in range(val):
                if (ind + (jump + 1)) < len(nums):
                    dp[ind + (jump + 1)] = min(dp[ind + (jump + 1)], dp[ind] + 1)
        
        return dp[len(nums)-1]