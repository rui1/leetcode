#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
def createList(filename):
    a_in= open(filename, encoding = 'utf-8')
    results =a_in.readlines()
    tl = list(map(int,''.join(results).replace('\n','').split(" ")))
    l = ListNode(tl[0])
    l.next = ListNode(tl[1])
    tmp=l.next
    for i in tl[2:]:
        tmp.next = ListNode(i)
        tmp=tmp.next
    printlist(l)
    print("ReverPrint")
    printReverse(l)
    '''print("True")
    printlist(l)
    print("Reversed")
    t=reverse1(l)
    printlist(t)'''
    '''print("Reversed_Rec")
    #printlist(l)
    s=reverse_Rec(l,None)
    printlist(s)'''
        

def printlist(l):
    if l is not None:
        print(l.val)
        printlist(l.next)
    

def reverse1(l):
    #print("Hello")
    pre = None
    tmp = l
    #printlist(tmp.next)
    while tmp is not None:
        tmp1 = tmp.next
        tmp.next = pre
        pre = tmp
        tmp = tmp1
    return pre

def reverse(l):
    #print("Hello")
    pre = None
    tmp = l
    #printlist(tmp.next)
    while tmp.next is not None:
        tmp1 = tmp.next
        tmp.next = pre
        pre = tmp
        tmp = tmp1
    tmp.next = pre
    return tmp

def reverse_Rec(l,pre):
    if l is None:
        return pre
    tmp=l.next
    l.next = pre
    return reverse_Rec(tmp,l)

def printReverse(l):
    if l is not None:
        printReverse(l.next)
        print(l.val)

createList("Testlist.txt")
