# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def divide(l):
            if len(l) == 1:
                return l[0]
            if len(l) == 0:
                return None
            m = len(l) // 2
            left = divide(l[:m])
            right = divide(l[m:])
            return merge(left, right)

        def merge(l1, l2):
            dummy = ListNode(0)
            temp = dummy
            while l1 and l2:
                if l1.val < l2.val:
                    temp.next = l1
                    l1 = l1.next
                else:
                    temp.next = l2
                    l2 = l2.next
                temp = temp.next
            
            if l1:
                temp.next = l1
            if l2:
                temp.next = l2
            
            return dummy.next
        return divide(lists)

