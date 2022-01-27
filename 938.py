# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root, low: int, high: int) -> int:

        cum = 0
        queue = [root]
        while len(queue) > 0:
            new_queue = []
            for cur in queue:
                if (cur.val - low) * (cur.val - high) <= 0:
                    cum += cur.val
                if cur.val > low and (cur.left is not None):
                    new_queue.append(cur.left)
                if cur.val < high and (cur.right is not None):
                    new_queue.append(cur.right)
            queue = new_queue
        return cum