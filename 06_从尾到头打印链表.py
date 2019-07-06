#!/usr/bin/python
# -*- coding:utf-8 -*-
#
# Copyright (c) 2019 github.com/zhoujl48, Inc. All Rights Reserved
#
"""
Project JianzhiOffer-Python -- 面试题06: 从尾到头打印链表

背景：无
要求：从尾到头打印链表。
输入：链表头节点
输出：反向打印

Usage: 
Authors: Zhou Jialiang
Email: zjl_sempre@163.com
Date: 2019-07-03
"""
class LinkNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


def gen_linked_list(arr):
    """初始化链表
    """
    if not arr:
        return None
    head = LinkNode(arr[0])
    if len(arr) > 1:
        cur = head
        for val in arr[1:]:
            cur.next = LinkNode(val)
            cur = cur.next
    return head


def print_linked_list(head):
    """打印链表
    """
    cur = head
    while cur:
        print(cur.val, end=' ')
        cur = cur.next
    print()


class Solution(object):
    def __init__(self):
        pass

    def reverse_stack(self, head):
        """反向打印链表(栈)
        """
        if not head:
            return
        stack = []
        cur = head
        while cur:
            stack.append(cur.val)
            cur = cur.next
        while stack:
            print(stack.pop(), end=' ')
        print()

    def reverse_recurse(self, head):
        """反向打印链表(递归)
        """
        if not head:
            return
        cur = head
        self._recurse(cur)
        print()

    def _recurse(self, cur):
        if not cur:
            return
        self._recurse(cur.next)
        print(cur.val, end=' ')


# 测试
if __name__ == '__main__':

    # 初始化链表并打印
    head = gen_linked_list([0, 1, 2, 3, 4])
    print('正向打印:\t', end=' ')
    print_linked_list(head)

    # 反向打印链表
    s = Solution()
    print('反向打印(栈):\t', end=' ')
    s.reverse_stack(head)
    print('反向打印(递归):\t', end=' ')
    s.reverse_recurse(head)

