import math


def flip(arr, k):
  pivot = math.floor((k+1)/2)
  for i in range(0, k):
    arr[i], arr[k-i] = arr[k-i], arr[i]
    
def findMaxValIndex(arr, k):
  ans = 0
  for i in range(0, k+1): 
    if arr[i] > arr[ans]:
      ans = i
  return ans
    
def pancake_sort(arr):
  for i in range(len(arr)-1, 0, -1):
    maxIndex = findMaxValIndex(arr, i)
    flip(arr, maxIndex)
    flip(arr, i)
  return arr


print(pancake_sort([2,1]))

def mut(i):
  return "hi"
    
def odd(i):
  return bool(i%2)
  
a = list(range(0,10))

print([x for x in a if odd(x)])

print([mut(x) for x in a])

print(sorted([1,5,4]))
print(str(1.4))
print(int(float("1.7")))

