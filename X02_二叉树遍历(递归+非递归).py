#!/usr/bin/python
# -*- coding:utf-8 -*-
#
# Copyright (c) 2019 github.com/zhoujl48, Inc. All Rights Reserved
#
"""
Project JianzhiOffer-Python -- 其它: 二叉树遍历(递归+非递归)

背景：无
要求：二叉树遍历
输入：root
输出：要求的遍历序列

例如输入二叉树为：
            1
          /   \
        2       3
       / \     /
      4   5   6

则输出：

Usage: 
Authors: Zhou Jialiang
Email: zjl_sempre@163.com
Date: 2019-07-11
"""
class BinaryTreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        pass

    def pre_order(self, node):
        if not node:
            return
        print(node.val, end=' ')
        if node.left:
            self.pre_order(node.left)
        if node.right:
            self.pre_order(node.right)

    def pre_order_stack(self, node):
        stack = []
        while stack or node:
            while node:
                print(node.val, end=' ')
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right

    def in_order(self, node):
        if not node:
            return
        if node.left:
            self.in_order(node.left)
        print(node.val, end=' ')
        if node.right:
            self.in_order(node.right)

    def in_order_stack(self, node):
        stack = []
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            print(node.val, end=' ')
            node = node.right

    def post_order(self, node):
        if not node:
            return
        if node.left:
            self.post_order(node.left)
        if node.right:
            self.post_order(node.right)
        print(node.val, end=' ')

    def post_order_stack(self, node):
        if not node:
            return
        stack_1, stack_2 = [], []
        stack_1.append(node)
        while stack_1:
            node = stack_1.pop()
            if node.left:
                stack_1.append(node.left)
            if node.right:
                stack_1.append(node.right)
            stack_2.append(node)
        while stack_2:
            print(stack_2.pop().val, end=' ')


# 测试
if __name__ == '__main__':

    # 初始化二叉树
    nodes = []
    for val in range(0, 8):
        nodes.append(BinaryTreeNode(val))
    nodes[1].left, nodes[1].right = nodes[2], nodes[3]
    nodes[2].left, nodes[2].right = nodes[4], nodes[5]
    nodes[3].left = nodes[6]

    # 层序打印镜像前后的二叉树
    s = Solution()
    print('先序遍历(递归)：', end='\t')
    s.pre_order(nodes[1])
    print('\n先序遍历(非递归)：', end='\t')
    s.pre_order_stack(nodes[1])
    print('\n中序遍历(递归)：', end='\t')
    s.in_order(nodes[1])
    print('\n中序遍历(非递归)：', end='\t')
    s.in_order_stack(nodes[1])
    print('\n后序遍历(递归)：', end='\t')
    s.post_order(nodes[1])
    print('\n后序遍历(非递归)：', end='\t')
    s.post_order_stack(nodes[1])

