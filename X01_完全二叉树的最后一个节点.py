#!/usr/bin/python
# -*- coding:utf-8 -*-
#
# Copyright (c) 2019 github.com/zhoujl48, Inc. All Rights Reserved
#
"""
Project JianzhiOffer-Python -- 其它: 完全二叉树的最后一个节点

背景：无
要求：求完全二叉树的最后一个节点
输入：root
输出：最后一个节点的值

例如输入二叉树为：
            1
          /   \
        2       3
       / \     /
      4   5   6

则输出：6

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

    def last(self, node):

        # 求深度
        depth, cur = 0, node
        while cur:
            depth += 1
            cur = cur.left

        # 求最后一个节点
        level, tmp_depth = 0, 0
        while node:
            level += 1
            if level == depth:  # 等于深度，直接返回
                return node
            cur = node
            if cur.right:
                p_cur, cur = cur, cur.right     # 前后两个指针跟随 当前左节点cur 和 父节点p_cur
                tmp_depth = level + 1           # 当前节点cur的深度
                while cur.left:                 # 从左搜索直至最底
                    p_cur, cur = cur, cur.left
                    tmp_depth += 1
                if tmp_depth < depth:           # 若层数小雨总层数，说明root.right子树不包含最后一个节点
                    node = node.left
                elif not p_cur.right:           # 若已达最后一层，且父节点p_cur无右孩子，则直接返回cur
                    return cur
                else:                           # (关键)若已达最后一层，且父节点p_cur有右孩子，
                    node = node.right           # 则直接root = root.right迭代即可
            else:
                node = node.left

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
    for val in range(0, 8):
        nodes.append(BinaryTreeNode(val))
    nodes[1].left, nodes[1].right = nodes[2], nodes[3]
    nodes[2].left, nodes[2].right = nodes[4], nodes[5]
    nodes[3].left = nodes[6]

    # 层序打印镜像前后的二叉树
    s = Solution()
    s.print_layer_with_newline(nodes[1])
    print('Last node value of node[{}]: {}'.format(1, s.last(nodes[1]).val))
    print('Last node value of node[{}]: {}'.format(2, s.last(nodes[2]).val))

