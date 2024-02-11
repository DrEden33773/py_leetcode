from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def o1Space(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        def len(head: ListNode) -> int:
            curr, res = head, 0
            while curr:
                res += 1
                curr = curr.next
            return res

        def jump(head: ListNode, steps: int) -> Optional[ListNode]:
            curr = head
            for _ in range(steps):
                if curr:
                    curr = curr.next
                else:
                    break
            return curr

        lenA, lenB = len(headA), len(headB)
        currA = jump(headA, lenA - lenB) if lenA > lenB else headA
        currB = jump(headB, lenB - lenA) if lenB > lenA else headB

        # now, with total same length, we can iterate over both lists
        while currA and currB:
            if currA == currB:
                return currA
            currA, currB = currA.next, currB.next

    def oNSpace(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        cached_code = set[ListNode]()
        currA, currB = headA, headB
        # iterate over currA
        while currA:
            cached_code.add(currA)
            currA = currA.next
        # iterate over currB, with a check if the node is in the set
        while currB:
            if currB in cached_code:
                return currB
            currB = currB.next

    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        return self.o1Space(headA, headB)
