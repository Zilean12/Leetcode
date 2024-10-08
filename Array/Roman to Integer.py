class Solution(object):
    def romanToInt(self, s):
        roman_to_int = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        total = 0
        i = 0
        while i < len(s):
            if i + 1 < len(s) and roman_to_int[s[i]] < roman_to_int[s[i + 1]]:
                total += roman_to_int[s[i + 1]] - roman_to_int[s[i]]
                i += 2
            else:
                total += roman_to_int[s[i]]
                i += 1
        print("Integer:", total)
        return total
solution = Solution()

test_cases = ["III", "IV", "IX", "LVIII", "MCMXCIV"]
for case in test_cases:
    print(f"Roman numeral: {case}, Integer: {solution.romanToInt(case)}")