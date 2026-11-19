# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Queue?
        # add root -> remove left = root -> add children
        if not root:
            return []

        res = []
        queue = deque([root])
        count_children = 1

        while queue:
            count = count_children
            count_children = 0
            nest = []
            while count: # while there are nodes from the first layer
                node = queue.popleft() # pop the furthest to the l
                nest.append(node.val)
                if node.left:
                    queue.append(node.left)
                    count_children += 1
                if node.right:
                    queue.append(node.right)
                    count_children += 1 
                count -= 1
            res.append(nest)
        
        return res