# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        flag = 0
        newList = tempHead = ListNode()
        while head and head.next:
            currSum = head.val
            head = head.next
            while head.val!=0:
                currSum+= head.val
                head = head.next
            currNode = ListNode(currSum,None)
            tempHead.next = currNode
            tempHead = tempHead.next
        return newList.next
            

