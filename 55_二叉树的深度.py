#!/usr/bin/python
# -*- coding:utf-8 -*-
#
# Copyright (c) 2019 github.com/zhoujl48, Inc. All Rights Reserved
#
"""
Project JianzhiOffer-Python -- 面试题55: 二叉树的深度/判断平衡二叉树

1. 二叉树的深度
背景：从根节点到叶节点依次经过的节点形成树的一条路径，最长路径的长度为树的深度
要求：求二叉树的深度
输入：root
输出：二叉树的深度

例如输入二叉树为：
            1
          /   \
        2       3
       / \       \
      4   5       6
         /
        7
则输出深度为：4

2. 判断平衡二叉树
背景：如果二叉树中任意节点的左、右子树的深度相差不超过1，那么它就是一棵平衡二叉树
要求：判断是否为平衡二叉树
输入：root
输出：True/False

例如输入二叉树为：
            1
          /   \
        2       3
       / \       \
      4   5       6
         /
        7
则输出深度为：True

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

    def depth(self, node):
        """二叉树深度
        """
        if not node:
            return 0
        return 1 + max(self.depth(node.left), self.depth(node.right))

    def is_balance(self, node):
        """判断是否平衡二叉树(重复计算深度)
        """
        if not node:
            return True
        if abs(self.depth(node.left) - self.depth(node.right)) <= 1:
            return self.is_balance(node.left) and self.is_balance(node.right)
        return False

    def _aux_is_balance_postorder(self, node):
        """功能函数：判断是否平衡二叉树(无重复计算深度)
        """
        if not node:
            return True, 0
        left_is_balance, left_depth = self._aux_is_balance_postorder(node.left)
        right_is_balance, right_depth = self._aux_is_balance_postorder(node.right)
        if left_is_balance and right_is_balance:
            if abs(left_depth - right_depth) <= 1:
                return True, max(left_depth, right_depth) + 1
        return False, -1

    def is_balance_postorder(self, node):
        """统一接口：判断是否平衡二叉树(无重复计算深度)
        """
        is_balance, depth = self._aux_is_balance_postorder(node)
        return is_balance

    def print_layer_with_newline(self, root):
        """层序打印(用于方便测试二叉树输出)
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
    nodes[5].left = nodes[7]
    nodes[3].right = nodes[6]

    # 若注释，则输入示例变为平衡二叉树，否则不是平衡二叉树，用于测试
    nodes[2].left = None

    # 层序打印镜像前后的二叉树
    s = Solution()
    s.print_layer_with_newline(nodes[1])
    print('Max depth of node[{}]: {}'.format(1, s.depth(nodes[1])))
    print('Max depth of node[{}]: {}'.format(2, s.depth(nodes[2])))
    print('Max depth of node[{}]: {}'.format(5, s.depth(nodes[5])))
    print('Node[{}] is Balance: {}'.format(1, s.is_balance(nodes[1])))
    print('Node[{}] is Balance: {}'.format(1, s.is_balance_postorder(nodes[1])))

