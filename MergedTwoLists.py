def mergeTwoLists(self,l1,l2):
        if l1 is None:
            ret = l2
        elif l2 is None:
            ret =l1
        elif l1.val<l2.val:
            ret = l1
            self.merge(l1.next,l2,l1)
        else:
            ret =l2
            self.merge(l1,l2.next,l2)
        return ret

            
def merge(self, l1,l2,pre):
    if l1 is None:
        pre.next = l2
        return
    elif l2 is None:
        pre.next = l1
        return
    elif l1.val>l2.val:
        tmp =l2.next
        l2.next = l1
        tmp1 = l1
        pre.next=l2
        self.merge(tmp1,tmp,l2)
    elif l1.val<=l2.val:
        tmp1=l1.next
        l1.next = l2
        tmp=l2
        pre.next = l1
        self.merge(tmp1,tmp,l1)


            
