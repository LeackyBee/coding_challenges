from typing import List, Optional
from Utils.list import ListNode

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # O(n*k) time, but O(1) space
        output = ListNode()
        head = output
        while True:
            min_i = 0
            min_val = None
            i = 0
            while i < len(lists):
                node = lists[i]

                if node and (min_val is None or node.val < min_val):
                    min_i = i
                    min_val = node.val

                i += 1

            if min_val is None:
                break
            head.next = lists[min_i]
            head = head.next
            lists[min_i] = lists[min_i].next

        return output.next
