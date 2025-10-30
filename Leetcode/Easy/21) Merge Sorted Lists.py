from typing import Optional

from Utils.list import ListNode


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        output = ListNode()
        head = output

        while list1 and list2:
            if list1.val < list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next
            head = head.next

        if list1:
            head.next = list1
        elif list2:
            head.next = list2

        return output.next

if __name__ == "__main__":
    solution = Solution()
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    output = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4))))))
    assert solution.mergeTwoLists(list1, list2) == output