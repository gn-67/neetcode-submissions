# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find starting point
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next #start of second half 
        slow.next = None 
        prev = None

        #reverse second half
        while second:
            temp = second.next
            second.next = prev
            #shift up
            prev = second
            second = temp

        #merge two halves
        second = prev #beginning of second list, second is set to 
        first = head

        #keep going until second half runs out, then we just add the remaining one from first list
        while second: 
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1 #which is the next of list 1, flip flopping
            #shift pointers

            first = temp1 
            second = temp2

        








