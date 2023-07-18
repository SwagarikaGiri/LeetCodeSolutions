# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        value = ''
        current = head
        while(current):
            value = value+str(current.val)
            current = current.next
        rev = value[::-1]
        if value == rev:
            return True
        else:
            return False