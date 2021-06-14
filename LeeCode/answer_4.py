############
# 编写一个函数来查找字符串数组中的最长公共前缀。
#
# 如果不存在公共前缀，返回空字符串 ""。
#
# https://leetcode-cn.com/problems/longest-common-prefix/
##################
from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs.__len__() == 0:
            return ""
        str_0 = strs[0]
        index = 0
        is_prefix = True
        for i in range(0,len(str_0)):
            index = i+1
            tmp_str = str_0[:i+1]
            for str in strs:
                if not str.startswith(tmp_str):
                    is_prefix = False
                    break
            if not is_prefix :
                break
        return str_0[:index] if is_prefix else str_0[:index-1]


if __name__   == "__main__":
    str_list = "abcd"
    str_list1 = ["flower","flow","flight"]
    str_list2 = ["dog","racecar","car"]
    str_list3 = ["a"]
    #print(str_list[:0])
    #print("a".startswith(""))
    solution = Solution()
    print(solution.longestCommonPrefix(str_list3))
