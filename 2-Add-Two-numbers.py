# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        value1 =[]
        current = l1
        value2 =[]
        while current != None:
            value1.append(str(current.val))
            current = current.next

        current = l2
        while current != None:
            value2.append(str(current.val))
            current = current.next
      
        value1.reverse()
        value2.reverse()
      
        num1 = int("".join(value1))
        num2 = int("".join(value2))
 
        res = num1 + num2
        print(res)
        result = [int(x) for x in str(res)]
        print(result)
        result.reverse()
        headNode = ListNode(0,None)
        currentNode = headNode
        for i in range(0,len(result)-1):
            nextNode= ListNode(0,None)
            currentNode.val = result[i]
            currentNode.next = nextNode
            currentNode=nextNode
            print(headNode)
        currentNode.val = result[-1]

           
        return headNode

        


        
        


