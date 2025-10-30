from typing import Optional

from Utils.list import ListNode


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        # keep track of the start
        output = head
        # keep track of where our sorted list ends - first element can be assumed to be correct
        curr = head.next
        # keep track of what the last value was
        prev = head.val

        while curr:
            # new value, so append this to the list
            if curr.val != prev:
                head.next = curr
                head = head.next
            prev = curr.val
            curr = curr.next

        # cut off the end
        head.next = None

        return output

