# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
#     def addTwoNumbers(self, l1, l2, carry =0):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         val = l1.val + l2.val + carry
#         #divide by 10 and floor to int
#         # 7//10 = 0
#         # 17//10 = 1
#         carry = val // 10
#         # 7%10 = 7
#         # 18%10 = 8
#         node = ListNode(val % 10)
        
#         # xx + xxx
#         # xxx + xx
#         # xxx + xxx with c = 1
        
#         if l1.next is not None or l2.next is not None or carry != 0:
#             if l1.next is None:
#                 l1.next = ListNode(0)
#             if l2.next is None:
#                 l2.next = ListNode(0)
#             node.next = self.addTwoNumbers(l1.next, l2.next, carry)
            
#         return node
    
    def addTwoNumbers(self, l1, l2, c = 0):
        head = ListNode(0)
        temp = head

        # c == 1 is true
        while l1 or l2 or c:
            if l1 is None:
                l1 = ListNode(0)
            if l2 is None:
                l2 = ListNode(0)
            print(l1.val, l2.val)
            val =  l1.val + l2.val + c
            c = val // 10
            temp.next = ListNode(val % 10)
            temp = temp.next 
            l1 = l1.next
            l2 = l2.next
        
        return head.next
    

    

l1 = NodeList(2)
l1.next = NodeList(4)
l1.next.next = NodeList(3)

l2 = NodeList(5)
l2.next = NodeList(6)
l2.next.next = NodeList(4)

main(l1,l2)