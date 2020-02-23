#remove k digit to minimize number
class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        
#         12345264
#              ^         
#           ^
        
        
        stack = list()
        
        
        for digit in num:
            #check if the element before is bigger
            #keep going till num[d-1] < num[d] 
            while k and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        
        #if there is K left then the array is 100% in ASCENDING order
        final = stack[:-k] if k else stack
        
        return "".join(final).lstrip('0') or '0'