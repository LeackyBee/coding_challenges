from typing import Any, Optional


def list_from_array(list:list[Any]):
    if not list:
        return None
    output = ListNode(list[0])
    head = output
    for i in list[1:]:
        head.next = ListNode(i)
        head = head.next
    return output


class ListNode:
    def __init__(self, val:Any=0, next:Optional['ListNode']=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{self.val}, {self.next}"

    def __eq__(self, other):
        return self.val == other.val and self.next == other.next
