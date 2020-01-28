import collections

"""
Node
"""
class Node:
    def __init__(self):
        self.val = 1
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


"""
Stack
"""

stack = list()

stack.append(1)
stack.pop()



"""
Queue
"""

stack = list()

stack.append(1)

#pop from the front
stack.pop(0)


