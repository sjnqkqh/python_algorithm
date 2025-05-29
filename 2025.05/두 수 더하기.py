from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"ListNode({self.val}, {self.next})"


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    result = ListNode(0)
    mod = 0
    while l1 or l2:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        temp = val1 + val2 + result.val
        mod = temp // 10
        temp = temp % 10

        l1 = l1.next if l1 is not None else None
        l2 = l2.next if l2 is not None else None

        result.next = ListNode(temp)
        result = result.next

        if l1 is None and l2 is None and temp == 0 and mod == 1:
            result.next = ListNode(1, None)

        print(result)

    return result


result = addTwoNumbers(ListNode(2, ListNode(4, ListNode(3, None)))
                       , ListNode(5, ListNode(6, ListNode(4, None))))
# print(result)
# addTwoNumbers(ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, None)))))))
#               , ListNode(9, ListNode(9, ListNode(9, ListNode(9, None)))))
addTwoNumbers(ListNode(0), ListNode(0))
