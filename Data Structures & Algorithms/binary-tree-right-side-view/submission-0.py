# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        def bfs(root):
            if not root:
                return []
            
            res = []
            queue = deque([root])

            while queue:
                level_size = len(queue)
                current_level = []
                for _ in range(level_size):
                    node = queue.popleft()
                    current_level.append(node)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                res.append(current_level[len(current_level) - 1].val)
            return res
        return bfs(root)
