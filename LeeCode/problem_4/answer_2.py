from typing import List
import pytest
'''
    思想：利用三指针方法。一个指向组合体的末端，2个分别指向nums1和nums2的末端。
         从nums2的末端开始和nums1的末端比较，将最大值放到组合体的末端。这样可以减少元素交换的次数。
    细节：
        1、Python中没有++ --等操作符。
        2、i+=1 与i=i+1的区别：
            1）对于不可变对象int str tuple等，每调用一次都会给i分配一个地址。
                i=0
                print(id(i))
                i=i+1
                print(id(i))
                i+=1
                print(id(i))
            2）对于可变类型对象 i+=1不会改变内存地址；i=i+1 会改变内存地址。
                list_tmp = [1,2,3]
                print(id(list_tmp))
                list_tmp +=[4]
                print(id(list_tmp))
                list_tmp = list_tmp + [5]
                print(id(list_tmp))
        
'''


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_end = m - 1
        nums2_end = n - 1
        num_end = m + n - 1
        while nums2_end >= 0:
            if nums1_end >= 0 and nums1[nums1_end] > nums2[nums2_end]:
                nums1[num_end] = nums1[nums1_end]
                num_end = num_end - 1
                nums1_end = nums1_end - 1
            else:
                nums1[num_end] = nums2[nums2_end]
                num_end = num_end - 1
                nums2_end = nums2_end - 1


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
