# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack_1 = []
        stack_2 = []
        cur1 = l1
        cur2 = l2
        while cur1:
            stack_1.append(cur1.val)
            cur1 = cur1.next
        while cur2:
            stack_2.append(cur2.val)
            cur2 = cur2.next
       
        carry = 0
        head = None
        #Now add
        while stack_1 or stack_2 or carry:
            val_1 = stack_1.pop() if stack_1 else 0
            val_2 = stack_2.pop() if stack_2 else 0

            total = val_1 + val_2 + carry
            carry = total//10
            digit = total%10
        
            Node = ListNode(digit)
            Node.next = head
            head = Node
        return head