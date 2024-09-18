from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        pointer = None

        while (list1 or list2):
            tmp = None
            if (list1 and (not list2 or list1.val <= list2.val)):
                tmp = list1
                list1 = list1.next
            else:
                tmp = list2
                list2 = list2.next

            if not head:
                head = tmp
                pointer = head
            else:
                pointer.next = tmp
                pointer = tmp

        return head


if __name__ == "__main__":
    s = Solution()

    f = ListNode(5)
    e = ListNode(3, f)
    d = ListNode(1, e)

    c = ListNode(4)
    b = ListNode(2, c)
    a = ListNode(1, b)


assert s.mergeTwoLists(a, d).next.val == 1
