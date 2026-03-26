# https://leetcode.com/problems/add-two-numbers/ || Oms
def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c1 = l1
        c2 = l2
        res = ListNode(0)
        cur = res
        carry = 0
        while c2 or c1 or carry:
            v1 = c1.val if c1 else 0
            v2 = c2.val if c2 else 0
            total = v1+v2+carry
            carry = total//10
            cur.next = ListNode(total%10)
            cur = cur.next
            if c1:
                c1 = c1.next
            if c2:
                c2 = c2.next
        return res.next