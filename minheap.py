#https://leetcode.com/problems/kth-largest-element-in-a-stream/submissions/
import heapq
class KthLargest(object):
    
    #len(nums) >= k-1
    # 0 == 1-1
    
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.heap = nums
        self.k = k
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(nums)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        
        #len(nums) >= k-1
        # 0 == 1-1
        #to handle empty array
        #want to have len == k
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        #if we len == k 
        #val is bigger than the smallest than we swap
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val)
            
        return self.heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
def test_heap():
    kl = KthLargest(3,[4,5,8,2])
    #4,5,8
    assert kl.add(3) == 4
    #5,6,8
    assert kl.add(6) == 5
    #6,8,9
    assert kl.add(9) == 6

    kl = KthLargest(3,[])

    assert kl.add(5) == 5

    assert kl.add(4) == 4

    assert kl.add(3) == 3

    assert kl.add(1) == 3

    assert kl.add(2) == 3

    assert kl.add(6) == 4