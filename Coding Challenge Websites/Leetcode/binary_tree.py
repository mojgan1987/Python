# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def dfs(self, root):
    queue = [root]
    nodes = len(queue)

    while len(queue):
        for i in range(nodes):
            curr = queue.pop(0)
            print(curr.val)
            if curr.left is not None:
                self.dfs(curr.left)
            if curr.right is not None:
                self.dfs(curr.right)

def bfs(self, root):
    queue = [root]
    nodes = len(queue)

    while len(queue):
        for i in range(nodes):
            curr = queue.pop(0)
            print(curr.val)
            if curr.left is not None:
                queue.append(curr.left)
            if curr.right is not None:
                queue.append(curr.right)



