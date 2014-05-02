class TreeNode:
 def __init__(self, x):
     self.val = x
     self.left = None
     self.right = None
def sortedArrayToBST(num):
    if len(num)==0:
        return None
    elif len(num)<2:
        return TreeNode(num[0])
    else:
        mid = len(num)//2
        ret = TreeNode(num[mid])
        tmp = ret
        tmp1=ret
        i=mid-1
        while i<mid and i >=0:
            tmp.left = TreeNode(num[i])
            tmp = tmp.left
            i-=1
        j=mid+1
        while j>mid and j<len(num):
            tmp1.right = TreeNode(num[j])
            tmp1=tmp1.right
            j+=1
        return ret

def sortedArrayToBST_Rec(l,num):
    if len(num)
def printlist(l):
    if l is not None:
        printlist(l.left)
        print (l.val)
        printlist(l.right)
        
    
num = [1,3]
l=sortedArrayToBST(num)
printlist(l)
