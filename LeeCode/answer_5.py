# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
#
# 有效字符串需满足：
#
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 注意空字符串可被认为是有效字符串。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/valid-parentheses
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# https://leetcode-cn.com/problems/valid-parentheses/
class Solution:
    def isValid(self, s: str) -> bool:
        s_list = list(s)
        brackets_list = ["(", ")", "[", "]", "{", "}" ]

        if s_list.__len__() == 0:
            return True
        tmp_list = list()
        for i in range(len(s_list)):
            tmp_str = s_list[i]
            if tmp_list.__len__() == 0:
                tmp_list.append(tmp_str)
                continue
            if tmp_str in brackets_list:
                if self.match(tmp_list[-1], tmp_str):
                    tmp_list.pop()
                else:
                    tmp_list.append(tmp_str)
        return True if 0 == len(tmp_list) else False

    def match(self, str1, str2):
        if str1 == "(" and str2 == ")":
            return True
        elif str1 == "[" and str2 == "]":
            return True
        elif str1 == "{" and str2 == "}":
            return True
        else:
            return False

    def isValid_better(self, s: str) -> bool:
        brackets_dic = {"(":")", "[":"]", "{":"}" }
        stack = []
        for ch in s:
            if ch in brackets_dic:
                stack.append(ch)
            elif stack:
                if ch != brackets_dic[stack.pop()]:
                    return False
            else:
                return False

        return not stack


if __name__ == "__main__":
    str1 = "()"
    str2 = "()[]{}"
    str3 = "(]"
    str4 = "([)]"
    str5 = "{[]}"
    solution = Solution()
    print(solution.isValid_better(str5))
