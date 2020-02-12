import collections
import sys
import heapq

"""
Node
"""
class Node:
    def __init__(self):
        self.val = 1

"""
Sort
"""
a = [[10,20],[30,200],[400,50],[30,20]]
diff = lambda val: abs(val[0]-val[1])
sorted(a, key=diff, reverse= True)


"""
String
"""


"""
Int
"""

sys.maxint
-sys.maxint -1

"""
List
"""

print("\n======LIST=======\n")

intialize = [0] * 100


test = [[1,2],[1],[3]]

[1 in row for row in test ] #=> [true, true, true]
any((1 in row for row in test)) #=> false

for i in test:
    print(i)

for i in range(len(test)):
    print(i)


"""
Generator
"""

print("\n======GENERATOR=======\n")

my_comp = [x * 5 for x in range(1000) if x%2==0]
my_gen = (x * 5 for x in range(1000)if x%2==0)

print(sys.getsizeof(my_comp) > sys.getsizeof(my_gen))

def test():
    tuple = ((1,2), (3,4))
    for a, b in tuple:
        yield a, b

for i in test():
    print(i)


"""
Loop
"""

for i in range(10,0, -1):
    pass
    # print(i)

"""
Dictionary
"""

dc = dict()
dc.get(1) # to prevent key error

dfc = collections.defaultdict(Node)
# print(dfc["asdf"].val)
"""
Boolean
"""
# bool(1) = True
# bool(0) = False
"""
String
"""
s = "string"

# print(s[::-1])
#get the last character
#s t r i n g
#0 1 2 3 4 5
#0 1 2 3 4 -1 to the end
print(s[-1:]) #=> "g"


"""
Tuple
"""

t = ("a", 1, "b")

print(t[1])

# we can just destruct
org = (1,2,3)
a,b,c = org
print(a)


"""
Stack
"""

stack = list()

stack.append(1)
stack.pop()


"""
Queue
"""
print("\n======Queue=======\n")
stack = list()

stack.append(1)

#pop from the front
stack.pop(0)


"""
Class
"""
print("\n======CLASS=======\n")
class Orange:
    def __init__(self, row, col, layer):
        self.row = row
        self.col = col
        self.layer = layer

        
"""
Heap
"""
print("\n======HEAP=======\n")
nums = [4,1,2,3]
heapq.heapify(nums)
print(nums)
heapq.heappush(nums,5)
print(nums)
heapq.heapreplace(nums,6)
print(nums)

"""
Args
"""

def arg(*arg): 
    for i in arg:
        print("arg:", i) 

def kwag(arg1, arg2, arg3): 
    print("arg1:", arg1) 
    print("arg2:", arg2) 
    print("arg3:", arg3) 

def kwag1(**argk):
    for k, v in argk.items():
        print(k, v)
      
# Now we can use *args or **kwargs to 
# pass arguments to this function :  
args = ("Geeks", "for", "Geeks") 
arg(*args) 
  
kwargs = {"arg1" : "Geeks", "arg2" : "for", "arg3" : "Geeks"} 
kwag(**kwargs)
kwag1(**kwargs)

