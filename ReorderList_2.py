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
    print("Reorder")
    printlist(l)

def printlist(l):
    if l is not None:
        print(l.val)
        printlist(l.next)
def reorderList(head):
    if head is None or head.next is None or head.next.next is None:
        return
    else:
        Mid = findMid_It(head.next, head.next.next)
        printlist(Mid)
        print("Mid Above")
        tmp=Mid.next
        printlist(tmp)
        print("rest")
        Mid.next =None
        rev= reverse_It(tmp)
        printlist(rev)
        print("reversed")
        tmp = head.next
        merge_It(tmp, rev,head)
        printlist(head)
        print("merge")
        return
        
def findMid(sNode,fNode):
    if fNode.next is None:
        return sNode
    elif fNode.next.next is None:
        return sNode
    else:
        return findMid(sNode.next, fNode.next.next)
def findMid_It(sNode, fNode):
    while fNode.next is not None and fNode.next.next is not None:
        sNode = sNode.next
        fNode= fNode.next.next
    return sNode
def reverse(Node,pre):
    if Node is None:
        return pre
    tmp=Node.next
    Node.next =pre
    return reverse(tmp, Node)


def reverse_It(l):
    if l is None and l.next is None:
        return l
    else:
        pre = None
        while l.next is not None:
            tmp1 = l.next
            l.next = pre
            pre = l
            l = tmp1
        l.next = pre
        return l
    
def merge(l1,l2,pre):
    if l2 is None:
        return
    elif l1 is None:
        pre.next = l2
        return 
    else:
        pre.next = l2
        tmp2=l2.next
        l2.next = l1
        return merge(l1.next,tmp2,l1)
def merge_It(tmp1,tmp2,pre):
    print("l1, l2")
    print(tmp1.val)
    print(tmp2.val)
    #tmp1 = l1
    #tmp2 = l2
    while tmp2 is not None and tmp1 is not None:
        print("pre",'tmp1','tmp2')
        print(pre.val, tmp1.val, tmp2.val)
        pre.next = tmp2
        nextTmp2 = tmp2.next
        tmp2.next = tmp1
        pre=tmp1
        nextTmp1 = tmp1.next
        tmp2=nextTmp2
        tmp1=nextTmp1
    if tmp1 is None:
        pre.next = tmp2

    
    return    
        
createList("TestList2.txt")
