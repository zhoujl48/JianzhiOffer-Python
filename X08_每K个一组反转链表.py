#!/usr/bin/python
# -*- coding:utf-8 -*-
#
# Copyright (c) 2019 github.com/zhoujl48, Inc. All Rights Reserved
#
"""
Project JianzhiOffer-Python -- 其它: 每k个一组反转链表

背景：无
要求：每k个一组反转链表
输入1：1 -> 2 -> 3 -> 4 -> 5, k = 2
输出1：2 -> 1 -> 4 -> 3 -> 5
输入2：1 -> 2 -> 3 -> 4 -> 5, k = 3
输出2：3 -> 2 -> 1 -> 4 -> 5

Usage: 
Authors: Zhou Jialiang
Email: zjl_sempre@163.com
Date: 2019-07-17
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

    def reverse_per_2(self, head):
        """每2个一组反转链表
        需要4个指针:
            p_cur: 记录当前组反转前的第1个节点
            p_next: 记录当前组反转前的第2个节点
            p_old: 记录上一组反转后的最后节点
            p_new: 记录下一组反转前的起始节点
        """
        if not head or not head.next:
            return head
        dummy = LinkNode(-1)
        dummy.next = head
        p_old, p_cur, p_next = dummy, head, head.next
        while p_cur and p_next:
            p_new = p_next.next     # 记录
            p_old.next, p_next.next, p_cur.next = p_next, p_cur, p_new
            p_old, p_cur = p_cur, p_cur.next
            if p_cur:
                p_next = p_cur.next
        return dummy.next

    def _op_reverse(self, node):
        """反转操作
        反转以node为头节点的链表,
        返回反转后的头节点
        """
        if not node or not node.next:
            return node
        p_cur, p_next = node, node.next
        p_cur.next = None
        while p_cur and p_next:
            p_next_new = p_next.next
            p_next.next = p_cur
            p_cur, p_next = p_next, p_next_new
        return p_cur

    def reverse_per_k(self, head, k):
        """每k个一组反转链表
        需要6个指针(3 + 3):
        (1 ~ 2: 由上一轮循环更新的)
            1. p_old_end: 记录上一组的末尾节点
            2. p_cur_start: 记录当前组反转前的起始节点
        (3 ~ 6:  由本轮循环产生的)
            3. p_cur_end: 记录当前组反转前的末尾节点
            4. p_cur_reversed_start: 记录当前组反转后的起始节点
            5. p_cur_reversed_end: 记录当前组反转后的末尾节点
            6. p_new_start: 记录下一组反转前的起始节点

        循环更新逻辑:
            1. 找末尾: 根据p_cur_start找到p_cur_end和p_new_start, 若不足k个则直接连接并返回
            2. 反转k: 断开尾部连接, 并反转当前链表
            3. 更新p: 让   p_old_end = p_cur_reversed_end
                          p_cur_start = p_new_start
        """
        dummy = LinkNode(-1)
        dummy.next = head
        p_old_end = dummy
        p_cur_start = dummy.next
        while p_cur_start:

            # 定位当前k个节点的末尾节点p_cur_end, 并保存下一组的头节点p_new_start
            # 若不足k个, 则将上一个末尾节点与当前起始节点连接，直接返回
            tmp_cnt = 1
            p_cur_end = p_cur_start
            while tmp_cnt < k:
                if not p_cur_end.next:
                    p_old_end.next = p_cur_start
                    return dummy.next
                p_cur_end = p_cur_end.next
                tmp_cnt += 1
            p_new_start = p_cur_end.next

            # 反转当前k个节点的链表
            p_cur_end.next = None
            p_cur_reversed_start, p_cur_reversed_end = self._op_reverse(p_cur_start), p_cur_start

            # 将上一组末尾节点与当前反转后的起始节点连接, 并更新三个指针
            p_old_end.next = p_cur_reversed_start
            p_old_end, p_cur_start = p_cur_reversed_end, p_new_start

        return dummy.next


# 测试
if __name__ == '__main__':

    s = Solution()
    head = gen_linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9])
    print_linked_list(head)
    print_linked_list(s.reverse_per_2(head))

    for k in range(1, 10):
        head = gen_linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9])
        print('k = {}, '.format(k), end='')
        print_linked_list(s.reverse_per_k(head, k))

