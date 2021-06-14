from typing import List

'''
    思想：由于重复元素个数大于n/2，所以将nums排序，中间的元素就是重复元素。
    细节：
        1. list.sort() 方法是在原列表上排序。
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        mid_index = int(nums.__len__() / 2)
        return nums[mid_index]


if __name__ == "__main__":
    tmp_list1 = [3, 2, 3]
    tmp_list2 = [2, 2, 1, 1, 1, 2, 2]
    solution = Solution()
    print(solution.majorityElement(tmp_list1))
