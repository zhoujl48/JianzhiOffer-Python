#!/usr/bin/python
# -*- coding:utf-8 -*-
#
# Copyright (c) 2019 github.com/zhoujl48, Inc. All Rights Reserved
#
"""
Project JianzhiOffer-Python -- 面试题52: 两个链表的第一个公共节点

背景：无
要求：求两个链表的第一个公共节点
输入：head_1, head_2
输出：common

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

    def reverse_stack(self, head_1, head_2):
        """第一个公共节点
        """
        if not head_1 or not head_2:
            return

        # 计算长度差值
        cur_1, cur_2 = head_1, head_2
        cnt_1, cnt_2 = 0, 0
        while cur_1:
            cnt_1 += 1
            cur_1 = cur_1.next
        while cur_2:
            cnt_2 += 1
            cur_2 = cur_2.next

        # 长链表指针先走(差值)步
        cur_1, cur_2 = head_1, head_2
        if cnt_1 > cnt_2:
            for _ in range(cnt_1 - cnt_2):
                cur_1 = cur_1.next
        else:
            for _ in range(cnt_2 - cnt_1):
                cur_2 = cur_2.next

        # 同时遍历，直至遇到公共节点并返回
        while cur_1 and cur_2:
            if cur_1 == cur_2:
                return cur_1
            cur_1, cur_2 = cur_1.next, cur_2.next

        return


# 测试
if __name__ == '__main__':

    # 初始化链表并打印
    head_1 = gen_linked_list([0, 3, 5])
    head_2 = gen_linked_list([1, 2, 4, 6])
    common_head = gen_linked_list([11, 12, 13])
    head_1.next.next.next = common_head
    head_2.next.next.next.next = common_head
    print('链表1:\t', end=' ')
    print_linked_list(head_1)
    print('链表2:\t', end=' ')
    print_linked_list(head_2)

    # 第一个公共节点
    s = Solution()
    print('第一个公共节点:\t', end=' ')
    common = s.reverse_stack(head_1, head_2)
    print(common.val)


