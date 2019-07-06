#!/usr/bin/python
# -*- coding:utf-8 -*-
#
# Copyright (c) 2019 github.com/zhoujl48, Inc. All Rights Reserved
#
"""
Project JianzhiOffer-Python -- 面试题32: 从上到下打印二叉树

背景：无
要求：从上到下打印二叉树
输入：head
输出：按层打印(每层换行或不换行均实现一个版本)

例如输入二叉树为：
            0
          /   \
        1       6
       / \     / \
     2     5  7   9
    / \      /   /
  3    4    8   10
则：
不换行输出：0 1 6 2 5 7 9 3 4 8
换行输出：
0
1 6
2 5 7 9
3 4 8

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

    def print_layer(self, head):
        """打印层序遍历(不换行)
        """
        if not head:
            return

        queue = [head]
        while queue:
            cur = queue.pop(0)
            print(cur.val, end=' ')
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        print()
        return

    def print_layer_with_newline(self, head):
        """打印层序遍历(新层换行)
        Params:
            cur: 当前弹出队列的节点
            last: 正在打印的当前行的末尾节点
            nlast: 队列中最新的节点
        换行逻辑:
            nlast始终等于队列中最新的节点
            if cur == last:
                换行
                last = nlast
        """
        if not head:
            return
        queue = [head]
        last, nlast = head, None
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
        print()
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

    # 层序打印
    s = Solution()
    s.print_layer(nodes[0])
    s.print_layer_with_newline(nodes[0])

