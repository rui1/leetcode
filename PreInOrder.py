import sys
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
        if len(preorder)==0 or len(inorder)==0:
            return None
        else:
            cur = None
            k =0
            l = []
            for i in range(len(preorder)):
                if i ==0:
                    ret = TreeNode(preorder[0])
                    l.append(ret)
                else:
                    t = TreeNode(preorder[i])
                    if len(l)>0 and cur is None:
                        l[-1].left = t
                    elif cur is not None:
                        cur.right=t
                    l.append(t)
                cnt = 0
                while k >=0 and k<len(inorder) and len(l)>0 and inorder[k]==l[-1].val:
                    cur =l.pop()
                    k+=1
                    cnt+=1
                if cnt==0:
                    cur = None
            return ret
def buildTree(preorder, inorder):
    if len(preorder)==0 or len(inorder)==0:
        return None
    else:
        cur = None
        k =0
        l = []
        for i in range(len(preorder)):
            if i ==0:
                ret = TreeNode(preorder[0])
                l.append(ret)
            else:
                t = TreeNode(preorder[i])
                print("t.val",t.val)
                if len(l)>0 and cur is None:
                    print("left")
                    l[-1].left = t
                    
                elif cur is not None:
                    print("right")
                    cur.right=t
                l.append(t)
            cnt = 0
            print(k,inorder[k],l[-1].val)
            while k >=0 and k<len(inorder) and len(l)>0 and inorder[k]==l[-1].val:
                print("pop")
                cur =l.pop()
                k+=1
                cnt+=1
            if cnt==0:
                cur = None
            else:
                print("cur",cur.val)
            '''for x in l:
                sys.stdout.write(str(x.val))
            print('')'''
            preorderPrint(ret)
            inorderPrint(ret)
        return ret

def preorderPrint(ret):
    if ret is not None:
        print(ret.val)
        preorderPrint(ret.left)
        preorderPrint(ret.right)

def inorderPrint(ret):
    if ret is not None:
        inorderPrint(ret.left)
        print(ret.val)
        inorderPrint(ret.right)

preorder = [1,2,4,5,6,7,3]
inorder = [4,2,6,5,7,1,3]

preorder = [1,2]
inorder = [1,2]

ret = buildTree(preorder,inorder)
preorderPrint(ret)
inorderPrint(ret)
