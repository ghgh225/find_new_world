from typing import List
import pytest

'''
    思想：将两个数组合并成一个，然后用数组的排序方法。
    细节：
        1、sort()和sorted()的区别
            1）sort是使用在list上的方法，属于列表的成员方法；sorted是可以对所有可迭代的对象进行排序操作。
            2）list的sort方法返回值是对已经存在的列表进行操作；sorted是內建方法，返回一个新的list，而不是在原来的基础上操作。
            3）sort使用方法：list.sort()；sorted的使用方法：sorted(object)

'''

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1[m + i] = nums2[i]
        nums1.sort()


def test_case1():
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    solution = Solution()
    solution.merge(nums1, m, nums2, n)
    print(nums1)
def test_case2():
    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    solution = Solution()
    solution.merge(nums1, m, nums2, n)
    print(nums1)
