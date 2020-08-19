# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 ==None :
            return l2
        elif l2 == None:
            return l1
        else:
            head= l = ListNode(None)   
            while l1 != None and l2 != None:
                # assigne the next node to smaller one
                if l1.val < l2.val:
                    l.next = l1
                    l1 = l1.next
                else:
                    l.next = l2
                    l2 = l2.next
                # move to the next node
                l = l.next                
            # attached the last one
            if l1:
                l.next = l1
            elif l2:
                l.next = l2
            return head.next
