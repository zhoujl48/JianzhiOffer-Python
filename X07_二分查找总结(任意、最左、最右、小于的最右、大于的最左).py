#!/usr/bin/python
# -*- coding:utf-8 -*-
#
# Copyright (c) 2019 github.com/zhoujl48, Inc. All Rights Reserved
#
"""
Project JianzhiOffer-Python -- 其它: 二分查找总结(任意、最左、最右、小于的最右、大于的最左)

背景：无
要求：二分查找最左最优目标索引以及目标个数
输入： [-4, -2, -1, 0, 1, 1, 1, 2, 3, 5], 1
输出：目标索引: 任意 = 5, 最左 = 4, 最右 = 6, 个数 = 3

-- 中位数总结 --

在区间范围的「二分」过程中, 若存在子区间包含用于比较划分的中位数索引mid,
则应区分「左中位数」或「右中位数」:
    当区间划分为[st, mid - 1]与[mid, ed]时, 为了能够让[mid, ed]缩到单个元素, 应使用右中位数: mid = st + (ed - st) // 2 + 1;
    当区间划分为[st, mid]与[mid + 1, ed]时, 为了能够让[st, mid]缩到单个元素, 应使用左中位数: mid = st + (ed - st) // 2;
    当区间被划分为[st, mid - 1]与[mid + 1, ed]时, 不必区分左/右中位数，因为区间必能缩到单个元素。

具体地:
    查找任意目标索引时, 采用左/右中位数均可;
    查找「最左目标索引」或「最左的大于目标元素的索引」时, 采用左中位数;
    查找「最右目标索引」或「最右的小于目标元素的索引」时, 采用右中位数。

Usage: 
Authors: Zhou Jialiang
Email: zjl_sempre@163.com
Date: 2019-07-13
"""
class Solution(object):
    def __init__(self):
        pass

    def find_random_target(self, arr, target, st, ed):
        while st < ed:
            # mid = st + (ed - st) // 2
            mid = st + (ed - st) // 2 + 1    # 此处用左中位数或右中位数均可
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                st = mid + 1
            else:
                ed = mid - 1
        return -1

    def find_left_target(self, arr, target, st, ed):
        while st < ed:
            mid = st + (ed - st) // 2        # 左中位数
            (st, ed) = (mid + 1, ed) if arr[mid] < target else (st, mid)
        if arr[st] == target:
            return st
        return -1

    def find_right_target(self, arr, target, st, ed):
        while st < ed:
            mid = st + (ed - st) // 2 + 1    # 右中位数
            (st, ed) = (st, mid - 1) if arr[mid] > target else (mid, ed)
        if arr[ed] == target:
            return ed
        return -1

    def cnt_target(self, arr, target, st, ed):
        i_min = self.find_left_target(arr, target, st, ed)
        if i_min != -1:
            i_max = self.find_right_target(arr, target, i_min, ed)
            return i_max - i_min + 1, i_min, i_max
        return 0, -1, -1

    def find_right_smaller_than_target(self, arr, target, st, ed):
        if not arr or arr[0] >= target:
            return -1
        while st < ed:
            mid = st + (ed - st) // 2 + 1   # 右中位数
            (st, ed) = (st, mid - 1) if arr[mid] >= target else (mid, ed)
        return ed

    def find_left_larger_than_target(self, arr, target, st, ed):
        if not arr or arr[ed] <= target:
            return -1
        while st < ed:
            mid = st + (ed - st) // 2       # 左中位数
            (st, ed) = (mid + 1, ed) if arr[mid] <= target else (st, mid)
        return st


# 测试
if __name__ == '__main__':
    s = Solution()
    arr = [-4, -2, -1, 0, 1, 1, 1, 2, 3, 5]
    for target in [0, 1, 4]:
        idx_random = s.find_random_target(arr, target, 0, len(arr) - 1)
        cnt, idx_left, idx_right = s.cnt_target(arr, target, 0, len(arr) - 1)
        idx_right_small = s.find_right_smaller_than_target(arr, target, 0, len(arr) - 1)
        idx_left_large = s.find_left_larger_than_target(arr, target, 0, len(arr) - 1)
        print('待搜索数组: {}, 目标: {}'.format(arr, target))
        print('目标索引: 任意 = {}, 最左 = {}, 最右 = {}, 个数 = {}'.format(idx_random, idx_left, idx_right, cnt))
        print('小于目标的最右索引: {}, 大于目标的最左索引: {}'.format(idx_right_small, idx_left_large))





