
from typing import List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverse(self, x: int) -> int:
        tmp = reversed(str(x))
        ret_list = list(tmp)
        if x >= 0 :
            symbol = ''
            ret_str = ''.join(ret_list)
        else:
            symbol = '-'
            ret_str = symbol + ''.join(ret_list[:-1])
        #print("ret_str is {}".format(ret_str))
        ret_int = int(ret_str)
        if ret_int > -2147483648 and ret_int < 2147483647:
            return ret_int
        else:
            return 0
    def reverse_better(self,x: int) -> int:
        y_int ,ret = abs(x),0
        #boundry 范围是[-2^31,2^31-1]
        boundry = (1<<31) -1 if x>0 else 1<<31

        while(y_int >0):
            ret = ret*10 + y_int%10
            if ret > boundry:
                return 0
            y_int = y_int //10

        return ret if x >0 else -ret




if __name__ == "__main__":
    sol = Solution()

    ret = sol.reverse_better(120)
    print(str(ret))
