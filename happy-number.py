class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        # Input: 19
        # Output: true
        # Explanation: 
        # 12 + 92 = 82
        # 82 + 22 = 68
        # 62 + 82 = 100
        # 12 + 02 + 02 = 1
        seen = set()
        res = 0
        while res != 1:
            res = 0
            while n:
                temp = n%10
                n //= 10
                res += temp ** 2
            if res in seen:
                return False
            seen.add(res) 
            n = res

        
        return True



sol = Solution()

print(sol.isHappy(19))
            


