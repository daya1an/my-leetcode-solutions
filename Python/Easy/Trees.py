#   Maximum Depth of Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# https://leetcode.com/problems/validate-binary-search-tree/

#my solution (3ms)
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stk = []
        prev = float('-inf')
        curr = root

        while curr or stk:
            while curr:
                stk.append(curr)
                curr = curr.left

            curr = stk.pop()

            if prev >= curr.val:
                return False

            prev = curr.val
            curr = curr.right

        return True


# 0ms solution
class Solution:
    def validate(self, node, low, high):
        if not node:
            return True

        if not (low < node.val < high):
            return False

        return self.validate(node.left, low, node.val) and self.validate(node.right, node.val, high)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validate(root, float('-inf'), float('inf'))