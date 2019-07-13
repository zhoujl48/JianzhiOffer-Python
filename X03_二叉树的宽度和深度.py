#!/usr/bin/python
# -*- coding:utf-8 -*-
#
# Copyright (c) 2019 github.com/zhoujl48, Inc. All Rights Reserved
#
"""
Project JianzhiOffer-Python -- 其它: 二叉树的宽度和深度

背景：无
要求：二叉树的宽度和深度
输入：root
输出：返回二叉树的宽度和深度

例如输入二叉树为：
            1
          /   \
        2       3
       / \     /
      4   5   6
         /
        7

则输出：depth = 4
       width = 3

Usage: 
Authors: Zhou Jialiang
Email: zjl_sempre@163.com
Date: 2019-07-13
"""
class BinaryTreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        pass

    def depth_recurse(self, node):
        """深度优先遍历求高度(递归)
        """
        if not node:
            return 0
        return 1 + max(self.depth_recurse(node.left), self.depth_recurse(node.right))
    
    def width_and_depth(self, node):
        """广度优先遍历(非递归，队列)
        借用'换行层序遍历'的思想，直接计算宽度和高度
        """
        if not node:
            return 0

        queue = [node]  # 广度优先遍历队列
        depth = 0       # 最大高度
        width = 1       # 最大宽度
        width_cur = 0   # 当前层宽度
        last = node     # 本层最后的节点(需换行的点)
        nlast = node    # 当前最新的入队列
        while queue:
            cur = queue.pop(0)
            if cur.left:
                queue.append(cur.left)
                nlast = cur.left
                width_cur += 1
            if cur.right:
                queue.append(cur.right)
                nlast = cur.right
                width_cur += 1
            if cur == last:     # 更新规则: 若当前节点cur等于本层最后节点last，
                last = nlast    #          则将last更新为下层最后节点nlast
                depth += 1
                width = max(width, width_cur)
                width_cur = 0
        return width, depth


# 测试
if __name__ == '__main__':

    # 初始化二叉树
    nodes = []
    for val in range(0, 8):
        nodes.append(BinaryTreeNode(val))
    nodes[1].left, nodes[1].right = nodes[2], nodes[3]
    nodes[2].left, nodes[2].right = nodes[4], nodes[5]
    nodes[3].left = nodes[6]
    nodes[5].left = nodes[7]

    # 层序打印镜像前后的二叉树
    s = Solution()
    print('深度优先搜索：高度 = {}'.format(s.depth_recurse(nodes[1])))
    print('广度优先搜索：高度 = {}，宽度 = {}'.format(s.width_and_depth(nodes[1])[1], s.width_and_depth(nodes[1])[0]))

