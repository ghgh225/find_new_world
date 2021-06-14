from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ret_list = list()
        for i in range(nums.__len__()):
            minus = target - nums[i]
            index = self.find_index(nums,minus)
            if -1 != index and i != index:
                ret_list.append(i)
                ret_list.append(index)
                break
        return ret_list

    def find_index(self,list:List[int],num:int) -> [int]:
        ret = -1
        for i in range(list.__len__()):
            if num == list[i] :
                ret = i
                break
        return ret


if __name__ == "__main__":
    solution = Solution()
    nums = [2,7,11,15]
    target = 9
    print(solution.twoSum(nums,target))