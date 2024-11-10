# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root, low: int, high: int) -> int:

        queue = [root]
        visited = [0]
        cur = root
        cum = 0
        while len(queue) > 0:
            if visited[-1] == 0:
                cum += cur.val if (cur.val - low) * (cur.val - high) <= 0 else 0
            if visited[-1] == 2:
                queue.pop()
                visited.pop()
                if len(queue) > 0:
                    cur = queue[-1]
                continue
            if (cur.left is not None) and (visited[-1] == 0):
                visited[-1] += 1
                if cur.val > low:
                    queue.append(cur.left)
                    visited.append(0)
                    cur = cur.left
            elif (cur.right is not None):
                visited[-1] += 1
                if cur.val < high:
                    visited.append(0)
                    queue.append(cur.right)
                    cur = cur.right
            else:
                queue.pop()
                visited.pop()
                if len(queue) > 0:
                    cur = queue[-1]
        return cum