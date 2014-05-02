class ListNode:
    def __init__(self,x):
        self.val = x
        self.next =None

def insertSortList(head):
    if head is None or head.next is None:
        return head
    else:
        sort= head
        while head is not None:
            l1 = sort
            l2 = head.next
            rest = l2.next
            while l1 != l2 and l2.val<l1.val:
                    l1.next = rest
                    l2.next = l2
            head = head.next


a=[1,2,3,4]
i=0
while a[i] <5:
    if a[i]==3:
        break
    print (a[i])
    i+=1
