class ListNode:
    def __init__(self,x):
        self.val= x
        self.next = None
def createList(filename):
    a_in=open(filename, encoding = 'utf-8')
    results = list(map(int,a_in.readlines()[0].replace('\n','').split()))
    l = ListNode(results[0])
    l.next = ListNode(results[1])
    tmp = l.next
    for i in results[2:]:
        tmp.next = ListNode(i)
        tmp = tmp.next
    printlist(l)
    reorderList(l)
    print("reorder")
    printlist(l)
def printlist(l):
    if l is not None:
        print(l.val)
        printlist(l.next)
def reorderList(head):
    if head is None or head.next is None or head.next.next is None:
        return
    else:
        tmp = head.next
        while tmp.next is not None:
            tmp=tmp.next
        printlist(head)
        tmp.next = head.next
        head.next = tmp
        reorderList(head.next.next)
        return
l=ListNode(1)
l.next =ListNode(2)
l.next.next =ListNode(3)
