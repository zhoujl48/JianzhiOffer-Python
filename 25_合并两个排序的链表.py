#!/usr/bin/python
# -*- coding:utf-8 -*-
#
# Copyright (c) 2019 github.com/zhoujl48, Inc. All Rights Reserved
#
"""
Project JianzhiOffer-Python -- 面试题25: 合并两个排序的链表

背景：无
要求：合并两个排序的链表
输入：head_1, head_2
输出：merged_head

Usage: 
Authors: Zhou Jialiang
Email: zjl_sempre@163.com
Date: 2019-07-04
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

    def merge_iter(self, head_1, head_2):
        """合并有序链表(迭代)
        """
        if not head_1:
            return head_2
        if not head_2:
            return head_1

        dummy = LinkNode(-1)
        cur = dummy
        cur_1, cur_2 = head_1, head_2
        while cur_1 and cur_2:
            (cur.next, cur_1, cur_2) = (cur_1, cur_1.next, cur_2) if cur_1.val < cur_2.val else (cur_2, cur_1, cur_2.next)
            cur = cur.next
        cur.next = cur_2 if not cur_1 else cur_1

        return dummy.next

    def merge_recurse(self, head_1, head_2):
        """合并有序链表(递归)
        """
        if not head_1:
            return head_2
        if not head_2:
            return head_1

        if head_1.val < head_2.val:
            merged_head = head_1
            merged_head.next = self.merge_recurse(head_1.next, head_2)
        else:
            merged_head = head_2
            merged_head.next = self.merge_recurse(head_1, head_2.next)

        return merged_head


# 测试
if __name__ == '__main__':

    # 初始化链表并打印
    head_1 = gen_linked_list([0, 3, 5, 7, 10])
    head_2 = gen_linked_list([1, 2, 4, 6, 8, 9])
    print('链表1:\t', end=' ')
    print_linked_list(head_1)
    print('链表2:\t', end=' ')
    print_linked_list(head_2)

    # 合并链表
    s = Solution()
    head_1 = gen_linked_list([0, 3, 5, 7, 10])
    head_2 = gen_linked_list([1, 2, 4, 6, 8, 9])
    head_merge_iter = s.merge_iter(head_1, head_2)
    print('合并(迭代法):\t', end=' ')
    print_linked_list(head_merge_iter)

    head_1 = gen_linked_list([0, 3, 5, 7, 10])
    head_2 = gen_linked_list([1, 2, 4, 6, 8, 9])
    head_merge_recurse = s.merge_recurse(head_1, head_2)
    print('合并(递归法):\t', end=' ')
    print_linked_list(head_merge_recurse)

