class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        hmap = {')':'(', ']': '[', '}': '{'}
        stack = list()
        for i in s:
            if i in hmap:
                top = stack.pop() if stack else "#"
                if top != hmap[i]:
                    return False
            else:
                stack.append(i)
        
        return False if stack else True
                