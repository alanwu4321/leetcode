#is Another Subtree
#Design Instagram


class Node: 
  
    # Constructor to create a new node 
    def __init__(self, data): 
        self.data = data  
        self.left = None
        self.right = None
  
# A utility function to check whether trees with roots 
# as root 1 and root2 are indetical or not 
def areIdentical(root1, root2): 
      
    # Base Case 
    if root1 is None and root2 is None: 
        return True
    if root1 is None or root2 is None: 
        return False
  
    # Check fi the data of both roots is same and data of 
    # left and right subtrees are also same 
    return (root1.data == root2.data and 
            areIdentical(root1.left , root2.left)and
            areIdentical(root1.right, root2.right) 
            )  
  
# This function returns True if S is a subtree of T, 
# otherwise False 
def isSubtree(T, S): 
      
    # Base Case 
    if S is None: 
        return True
  
    if T is None: 
        return False
  
    # Check the tree with root as current node 
    if (areIdentical(T, S)): 
        return True
  
    # IF the tree with root as current node doesn't match 
    # then try left and right subtreee one by one 
    return isSubtree(T.left, S) or isSubtree(T.right, S) 
  
  
# Driver program to test above function 
  
""" TREE 1 
     Construct the following tree 
              26 
            /   \ 
          10     3 
        /    \     \ 
      4      6      3 
       \ 
        30 
    """
  
T = Node(26) 
T.right = Node(3) 
T.right.right  = Node(3) 
T.left = Node(10) 
T.left.left = Node(4) 
T.left.left.right = Node(30) 
T.left.right = Node(6) 
  
""" TREE 2 
     Construct the following tree 
          10 
        /    \ 
      4      6 
       \ 
        30 
    """
S = Node(10) 
S.right = Node(6) 
S.left = Node(4) 
S.left.right = Node(30) 
  
if isSubtree(T, S): 
    print("Tree 2 is subtree of Tree 1")
else : 
    print("Tree 2 is not a subtree of Tree 1")
  
# This code is contributed by Nikhil Kumar Singh(nickzuck_007) 
