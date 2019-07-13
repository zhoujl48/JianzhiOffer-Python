#!/usr/bin/python
# -*- coding:utf-8 -*-
#
# Copyright (c) 2019 github.com/zhoujl48, Inc. All Rights Reserved
#
"""
Project JianzhiOffer-Python -- 其它: 合并无序链表

背景：无
要求：合并两个无序链表，并调整为有序
输入：l1: 3 -> 1 -> 4 -> 1, l2: 5 -> 9 -> 2 -> 6 ->5
输出：1 -> 1 -> 2 -> 3 -> 5 -> 5 -> 6 -> 9

Usage: 
Authors: Zhou Jialiang
Email: zjl_sempre@163.com
Date: 2019-07-13
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

    def merge_sorted(self, head_1, head_2):
        if not head_1:
            return head_2
        if not head_2:
            return head_1
        if head_1.val < head_2.val:
            merged_head = head_1
            merged_head.next = self.merge_sorted(head_1.next, head_2)
        else:
            merged_head = head_2
            merged_head.next = self.merge_sorted(head_1, head_2.next)
        return merged_head

    def _split(self, head):
        if not head:
            return None, None

        cur = head
        cnt = 0
        while cur:
            cur = cur.next
            cnt += 1
        cur = head
        for _ in range(cnt // 2 - 1):
            cur = cur.next
        mid = cur.next
        cur.next = None
        return head, mid

    def merge_unsorted(self, head_1, head_2):
        """归并排序的思想
        用_split()方法把无序链表从中间分成两部分
        直至分成单元素链表或空链表后，再回溯合并merge
        """
        if ((not head_1 or not head_1.next)
            and (not head_2 or not head_2.next)):
            return self.merge_sorted(head_1, head_2)
        head_1_st, head_1_mid = self._split(head_1)
        head_2_st, head_2_mid = self._split(head_2)
        return self.merge_sorted(self.merge_unsorted(head_1_st, head_1_mid), self.merge_unsorted(head_2_st, head_2_mid))


# 测试
if __name__ == '__main__':
    from numpy.random import choice, seed


    seed(0)
    s = Solution()
    for _ in range(5):
        head_1 = gen_linked_list(choice(range(10), size=5, replace=True).tolist())
        head_2 = gen_linked_list(choice(range(10), size=5, replace=True).tolist())
        print_linked_list(head_1)
        print_linked_list(head_2)
        print_linked_list(s.merge_unsorted(head_1, head_2))

