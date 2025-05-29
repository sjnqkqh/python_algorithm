# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"now: {self.val}, next: {self.next}"


from typing import Optional


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    result = ListNode(0)
    now = result
    rest = 0

    while l1 or l2:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        sum_result = val1 + val2 + rest
        rest = sum_result // 10

        now.next = ListNode(sum_result % 10)
        now = now.next

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

        if l1 is None and l2 is None and rest == 1:
            now.next = ListNode(1)

    return result.next


# print(addTwoNumbers(l1=ListNode(2, ListNode(4, ListNode(3))), l2=ListNode(5, ListNode(6, ListNode(4)))))
# addTwoNumbers(l1=ListNode(0), l2=ListNode(0))
print(addTwoNumbers(l1=ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9))))))),
              l2=ListNode(9, ListNode(9, ListNode(9, ListNode(9))))))
