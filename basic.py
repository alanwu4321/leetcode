import collections
import sys

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

any(a)
my_comp = [x * 5 for x in range(1000) if x%2==0]
my_gen = (x * 5 for x in range(1000)if x%2==0)

sys.getsizeof(my_comp) > sys.getsizeof(my_gen)

test = [[1,2],[1],[3]]

[1 in row for row in test ] #=> [true, true, true]
any((1 in row for row in test)) #=> false



"""
Loop
"""

for i in range(10,0, -1):
    pass
    # print(i)

"""
Dictionary
"""

dfc = collections.defaultdict(Node)
# print(dfc["asdf"].val)

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

