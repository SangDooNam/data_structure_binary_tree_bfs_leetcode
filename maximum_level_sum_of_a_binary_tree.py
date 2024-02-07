# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root):
        if not root:
            return None
        queue = deque([root])
        result = []
        while queue:
            n = len(queue)
            num = 0
            for i in range(n):
                node = queue.popleft()
                num += node.val
                

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(num)
        
        max_nums = max(result)
        return result.index(max_nums) + 1


def create_binary_tree(elements):
    root = TreeNode(elements.pop(0))
    queue = [root]
    
    while queue:
        node = queue.pop(0)
        left_val = elements.pop(0) if elements else None
        right_val = elements.pop(0) if elements else None
        if left_val is not None:
            node.left = TreeNode(left_val)
            queue.append(node.left)
        if right_val is not None:
            node.right = TreeNode(right_val)
            queue.append(node.right)
    return root

sol = Solution()
root = [1,7,0,7,-8,None,None]
# root = [989,None,10250,98693,-89388,None,None,None,-32127]
root = create_binary_tree(root)

print(sol.maxLevelSum(root))

