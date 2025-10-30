from typing import Optional, List

from Utils.list import ListNode
from Utils.logger import logger

"""
One possible optimisation I considered for this is exiting the loop early if only one list has values and carry is 0
We could then just set curr.next = list and be done, but this comes at a risk since those numbers are shared now
A solution to this is to deepcopy the list, but that operation is as expensive as the while loop, 
so instead we keep it simple and just iterate over the elements until we have no carry, l1, or l2
"""

def list_from_array(arr: List) -> ListNode:
    listNode = None
    for num in arr:
        listNode = ListNode(num, listNode)
    return listNode

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        output = ListNode(0, None) # init to this so we can set curr to a ListNode object.
        curr = output
        while carry or l1 or l2:
            total = 0
            if carry:
                total += carry
                carry = 0
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next

            if total > 9:
                total = total % 10
                carry = 1

            curr.next = ListNode(total, None)
            curr = curr.next
        return output.next

if __name__ == '__main__':
    solution = Solution()
    l1 = list_from_array([3,4,2])
    l2 = list_from_array([4,6,5])
    sol = solution.addTwoNumbers(l1, l2)
    assert sol == list_from_array([8,0,7])

    l1 = list_from_array([7,4,2])
    l2 = list_from_array([4,6,5])
    sol = solution.addTwoNumbers(l1, l2)
    logger.print(sol)
    assert sol == list_from_array([1,2,0,7])