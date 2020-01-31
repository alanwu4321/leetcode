
#https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        hset = set()
        hmap = dict()
        start = 0
        res = 0
        
        i, j =0,0
        
        
        #find where I last see the char and skip to the ch next to it
        for end, val in enumerate(s):
            if val in hmap:
                #skip to next index but if we already moved on (start is passed the next index) then start remain the same
                start = max(hmap[val] + 1, start)
            hmap[val] = end
            res = max(end-start + 1, res)
            
        
#         abba
        
#         val a
#         hmap a: 0
#         start 0
#         end 0 
#         res 1
        
#         val b
#         hmap a: 0, b:1
#         start 0
#         end 1
#         res 2
        
#         val b
#         #skip start to the last time we see b
#         hmap a: 0, b:2
#         start 2
#         end 2
#         res 2
        
#         val a
#         # a + 1 is smaller than our start so keep start = 2
#         hmap a: 0, b:2
#         start 2
#         end 3
#         res 2
        
#         val b
#         # b + 1 is bigger than our start so start = 3
#         hmap a: 0, b:4
#         start 3
#         end 4
#         res 2
            
        # for end, val in enumerate(s):
        #     if not val in hset:
        #         hset.add(val)
        #     else:
        #         print(hset, end, start)
        #         while s[start] != val:
        #             hset.remove(s[start])
        #             start += 1
        #         print(hset, end, start)
        #         start += 1
        #     res = max(end-start + 1, res)
        
        
        # while i < len(s) and j < len(s):
        #     if not s[j] in hset:
        #         hset.add(s[j])
        #         j+=1 
        #         res = max(res, j-i)
        #     #remove until s[j] is not in set
        #     else:
        #         hset.remove(s[i])
        #         i +=1

        return res
                
            
            
            