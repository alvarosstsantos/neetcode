from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        left, right = None, head

        while (right):
            tmp = right.next
            right.next = left
            left = right
            right = tmp

        return left


if __name__ == "__main__":
    s = Solution()

    d = ListNode()
    c = ListNode(1, d)
    b = ListNode(2, c)
    a = ListNode(3, b)

assert s.reverseList(a).val == 0
