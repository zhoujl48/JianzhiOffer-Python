#!/usr/bin/python
# -*- coding:utf-8 -*-
#
# Copyright (c) 2019 github.com/zhoujl48, Inc. All Rights Reserved
#
"""
Project JianzhiOffer-Python -- 面试题27: 二叉树的镜像

背景：无
要求：从上到下打印二叉树
输入：root
输出：镜像后的root

例如输入二叉树为：
            0
          /   \
        1       6
       / \     / \
     2     5  7   9
    / \      /
  3    4    8
则输出的镜像后二叉树为：
            0
          /   \
        6       1
       / \     / \
      9   7   5   2
           \     / \
            8   4   3

Usage: 
Authors: Zhou Jialiang
Email: zjl_sempre@163.com
Date: 2019-07-06
"""
class BinaryTreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        pass

    def mirror(self, node):
        """镜像二叉树
        """
        if (not node) or (not node.left and not node.right):
            return
        node.left, node.right = node.right, node.left
        if node.left:
            self.mirror(node.left)
        if node.right:
            self.mirror(node.right)
        return node

    def print_layer_with_newline(self, root):
        """层序打印(用于测试是否实现镜像功能)
        """
        if not root:
            return
        queue = [root]
        last, nlast = root, None
        while queue:
            cur = queue.pop(0)
            print(cur.val, end=' ')
            if cur.left:
                queue.append(cur.left)
                nlast = cur.left
            if cur.right:
                queue.append(cur.right)
                nlast = cur.right
            # 换行，更新标记
            if cur == last:
                print()
                last = nlast
        return

# 测试
if __name__ == '__main__':

    # 初始化二叉树
    nodes = []
    for val in range(10):
        nodes.append(BinaryTreeNode(val))
    nodes[0].left, nodes[0].right = nodes[1], nodes[6]
    nodes[1].left, nodes[1].right = nodes[2], nodes[5]
    nodes[2].left, nodes[2].right = nodes[3], nodes[4]
    nodes[6].left, nodes[6].right = nodes[7], nodes[9]
    nodes[7].left = nodes[8]

    # 层序打印镜像前后的二叉树
    s = Solution()
    s.print_layer_with_newline(nodes[0])
    s.print_layer_with_newline(s.mirror(nodes[0]))

