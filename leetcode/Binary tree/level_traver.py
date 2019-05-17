# #Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""通过队列来进行二叉树的层次遍历"""

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res=[]
        if not root :
            return res
        q=[root]
        while q:
            s=[]
            for i in range(len(q)):
                r=q.pop(0)
                s.append(r.val)
                if r.left:
                    q.append(r.left)
                if r.right:
                    q.append(r.right)
            res.append(s)
        return res