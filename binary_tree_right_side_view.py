from collections import deque 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def rightSideView(self, root):
        if not root:
            return []
        queue = deque([root])
        result = []
        while queue:
            n = len(queue)
            
            for i in range(n):
                node = queue.popleft()
                
                if i == n - 1:
                    result.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result


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

root = [1,2,3,None,5,None,4]
root = [1,None,3]
root = create_binary_tree(root)
sol = Solution()

print(sol.rightSideView(root))