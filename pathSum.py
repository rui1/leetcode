# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
 
class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def __init__(self):
        self.ret = []
    def pathSum(self, root, Sum):
        if root is None:
            return []
        self.findPath(root, [root.val], root.val, Sum)
        return self.ret
    def findPath(self, root,valList, curSum, Sum):
        if root.left is None and root.right is None and curSum ==Sum:
            self.ret.append(valList)
            return
        if root.left:
            self.findPath(root.left, valList+[root.left.val], curSum+root.left.val, Sum)
        if root.right:
            self.findPath(root.right, valList+[root.right.val],curSum+root.right.val, Sum)
            
            
            
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
 
class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, Sum):
        if root == None: return []
        Solution.res = []
        Solution.Sum = Sum
        self.getPath(root, [root.val], root.val)
        return Solution.res
         
    def getPath(self, root, valList, currSum):
        if root.left == None and root.right == None:
            if currSum == Solution.Sum: Solution.res.append(valList)
            return
        if root.left:
            self.getPath(root.left, valList + [root.left.val], currSum + root.left.val)
        if root.right:
            self.getPath(root.right, valList + [root.right.val], currSum + root.right.val)  