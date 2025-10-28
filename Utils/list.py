class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{self.val}, {self.next}"

    def __eq__(self, other):
        return self.val == other.val and self.next == other.next