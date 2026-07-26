# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head
        
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            curr = groupPrev
            i = 0
            while i < k and curr:
                curr = curr.next
                i += 1
            if curr is None:
                break
            if i != k:
                break
            currentHead = groupPrev.next
            restartNode = currentHead
            prev = curr.next
            stopNode = curr.next

            while currentHead != stopNode:
                nextNode = currentHead.next
                currentHead.next = prev
                prev = currentHead
                currentHead = nextNode
            groupPrev.next = prev
            groupPrev = restartNode
        return dummy.next