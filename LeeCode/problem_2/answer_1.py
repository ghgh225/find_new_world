from typing import List

'''
    思想：将nums中的元素与其出现的次数组合成一个字典。在判定字典中大于等n/2的结果。
    细节：
        1. for key in dict.keys() 方法遍历字典的key。
        2. for value in dict.values() 方法遍历字典的value。
        3. for key, value in dict.items() 方法遍历字典的kv。
        4. dict[key] = value ，如果dict中存在key，则更新对应value；如果没有，就新增key，并赋值value
        5. dict[key] 方法索引字典，如果存在key，就返回value；如果不存在，就报KeyError异常。
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        result_dic = dict()
        for item in nums:
            if item not in result_dic:
                result_dic[item] = 1
            else:
                result_dic[item] = result_dic[item] + 1
        #print(result_dic)
        for key, value in result_dic.items():
            if value >= nums.__len__() / 2:
                return key


if __name__ == "__main__":
    tmp_list1 = [3, 2, 3]
    tmp_list2 = [2, 2, 1, 1, 1, 2, 2]
    solution = Solution()
    print(solution.majorityElement(tmp_list2))
