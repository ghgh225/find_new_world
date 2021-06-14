# 罗马数字转整数

class Solution:
    def romanToInt(self, s: str) -> int:
        ret_int = 0
        oneworld_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        towworld_dict = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
        for key in towworld_dict.keys():
            while s.find(key) >= 0:
                ret_int = ret_int + towworld_dict[key]
                s = s.replace(key, " ", 1)

        for i in range(s.__len__()):
            if s[i] in oneworld_dict:
                ret_int = ret_int + int(oneworld_dict[s[i]])

        return ret_int


if __name__ == "__main__":
    test_str = "isisisisisisisis"
    test_str = test_str.replace("is", "aa", 2)
    # print(ret)
    print(test_str)
    sol = Solution()
    print(sol.romanToInt("MCMXCIV"))
    # towworld_dict = {'IV': 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
    # for key in towworld_dict.keys():
    #     print(key)
    #     print(towworld_dict[key])
