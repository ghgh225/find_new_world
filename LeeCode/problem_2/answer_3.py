from typing import List

'''
    思想：假设数组中每个不同的数字就代表一个国家，而数字的个数就代表这个国家的人数，他们在一起混战，就是每两个两个同归于尽。
         我们就可以知道那个人数大于数组长度一半的肯定会获胜。就算退一万步来说，其他的所有人都来攻击这个人数最多的国家，
         他们每两个两个同归于尽，最终剩下的也是那个众数。
'''


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        max_item = -1
        count = 0
        for item in nums:
            if count == 0:
                max_item = item
                count = count + 1
            elif max_item == item:
                count = count + 1
            else:
                count = count - 1
        return max_item


if __name__ == "__main__":
    tmp_list1 = [3, 2, 3]
    tmp_list2 = [2, 2, 1, 1, 1, 2, 2]
    tmp_list3 = [3, 3, 4]
    solution = Solution()
    print(solution.majorityElement(tmp_list3))
