class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if head is None  or head.next is None:
            return head
        ret = head.next
        head.next = ret.next
        ret.next = head
        self.swapPairsRec(head.next, head)
        return ret
    def swapPairsRec(self, head, pre):
        if head is None or head.next is None:
            return
        post = head.next
        pre.next = post
        head.next = post.next
        post.next = head
        return self.swapPairsRec(head.next, head)