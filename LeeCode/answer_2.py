#判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。


class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        x_list = list(x_str)
        x_len = x_list.__len__()
        index = 0
        while(index < x_len/2):
            if x_list[index] != x_list[x_len-1-index]:
                return False
            index = index +1

        return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome(121))

