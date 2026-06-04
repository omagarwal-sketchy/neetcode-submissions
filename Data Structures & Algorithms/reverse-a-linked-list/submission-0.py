# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count=0
        curr=head
        while curr!=None:
            curr=curr.next
            count+=1
        currnode=head
        for i in range(0,count):
            for j in range(0,count-i-1):
                newnode=currnode.next
                if newnode is not None:
                    buffer=currnode.val
                    currnode.val=newnode.val
                    newnode.val=buffer
                    currnode=newnode
            currnode=head
        return head
        