# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newHead = head
        while newHead.next:
            node1 = newHead
            node2 = newHead.next
            gcdValue = self.gcd(node1.val,node2.val)
            newNode = ListNode(gcdValue,node2)
            newHead.next =  newNode
            newHead = newHead.next.next
        return head


    # Recursive function to return gcd of a and b
    def gcd(self, a, b):
        # Everything divides 0
        if (a == 0):
            return b
        if (b == 0):
            return a
 
        # base case
        if (a == b):
            return a
 
        # a is greater
        if (a > b):
            return gcd(a-b, b)
        return gcd(a, b-a)
