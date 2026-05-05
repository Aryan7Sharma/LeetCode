# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k<1:return head
        length = 1
        copyhead=head
        while copyhead.next:
            length+=1
            copyhead=copyhead.next 
        if k>length:
            k = k%length
        for i in range(k):
            curr = head
            while curr.next.next:
                curr = curr.next
            last = curr.next
            curr.next = None
            last.next = head
            head = last
        return head

#### need to optimize this this is a brute force solution.
#### for optimization get the modulo of k%length that time it needs to rotate other than that is a circular. repeating.