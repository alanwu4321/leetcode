# 8,8,8,8,8,7,9,9,8=> 5,8,1,7,2,9,1,8

# 2,8,1,7
# has_next
# get_next

class decode:
    def __init__(self, earr):
        self.count = 0
        self.pointer = 0
        self.earr = earr
        
    def has_next(self):
        if self.pointer >= len(self.earr):
            return False
        return True
    
    def get_next(self):
        
        self.count += 1
        temp = self.earr[self.pointer + 1]
        #when we deplete the count
        if self.earr[self.pointer] <= self.count:
            if self.has_next():
                self.pointer += 2
                self.count = 0
            else: 
                raise Exception("out of range!")
        return temp
            
def encode(arr):
    if not arr: return []
    res = [1, arr[0]]
    for i in range(0, len(arr)-1):
        if arr[i] == arr[i+1]:
            res[-2] += 1
        else:
            res.append(1, arr[i+1])
    return res

arr1 = []
arr2 = [1,8]
arr3 = [5,-8,1,7,2,9]
arr4 = [5,8,1,7,2,9,1,8]

arr5 = [5,5,5]
assert encode(arr5) == [3,5]

dec = decode(arr4)

while(dec.has_next()):
    print(dec.get_next())