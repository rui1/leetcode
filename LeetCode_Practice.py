class Chaos:
    def __init__(self):
        self.list_value = []
        self.value = "default"
def reverseWords(self, s):
    t=s.strip().split()
    if len(t)==0:
        return ""
    else:
        t.reverse()
        return " ".join(t)
class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversalRec(self,root):
        if root is not None:
            self.inorderTraversalRec(root.left)
            self.list_value.append(root.val)
            self.inorderTraversalRec(root.right)
    def inorderTraversal(self, root):
        if root is None:
            return []
        else:
            self.inorderTraversalRec(root)
            return self.list_value
        
    def __init__(self):
        self.list_value = []
        self.value = 0 
