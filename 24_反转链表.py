#!/usr/bin/python
# -*- coding:utf-8 -*-
#
# Copyright (c) 2019 github.com/zhoujl48, Inc. All Rights Reserved
#
"""
Project JianzhiOffer-Python -- 面试题24: 反转链表

背景：无
要求：反转链表
输入：head
输出：reversed_head

Usage: 
Authors: Zhou Jialiang
Email: zjl_sempre@163.com
Date: 2019-07-06
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
        """反转链表(栈)
        """
        if not head or not head.next:
            return head

        stack = []
        while head:
            stack.append(head)
            head = head.next

        reversed_head = stack.pop()
        cur = reversed_head
        while stack:
            cur.next = stack.pop()
            cur = cur.next
        cur.next = None     # 反向末尾指空

        return reversed_head

    def reverse_direct(self, head):
        """反转链表(直接)
        """
        if not head or not head.next:
            return head

        pre, cur = head, head.next
        head.next = None    # 反向末尾指空
        while cur:
            next = cur.next
            cur.next = pre
            pre, cur = cur, next

        return pre


# 测试
if __name__ == '__main__':

    # 初始化链表并打印
    head_1 = gen_linked_list([0])
    head_2 = gen_linked_list([1, 2, 4, 6, 8, 9])
    print('链表1:\t', end=' ')
    print_linked_list(head_1)
    print('链表2:\t', end=' ')
    print_linked_list(head_2)

    # 合并链表
    s = Solution()
    print('反转链表1:\t', end=' ')
    reversed_head = s.reverse_stack(head_1)
    print_linked_list(reversed_head)
    reversed_head = s.reverse_stack(head_2)
    print('反转链表2:\t', end=' ')
    print_linked_list(reversed_head)

    head_1 = gen_linked_list([0])
    head_2 = gen_linked_list([1, 2, 4, 6, 8, 9])
    print('反转链表1:\t', end=' ')
    reversed_head = s.reverse_direct(head_1)
    print_linked_list(reversed_head)
    reversed_head = s.reverse_direct(head_2)
    print('反转链表2:\t', end=' ')
    print_linked_list(reversed_head)

