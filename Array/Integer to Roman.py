class Solution(object):
    def intToRoman(self, num):
        roman = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        integer = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        res = ""
        for i in range(len(integer)):
            while num >= integer[i]:
                num -= integer[i]
                res += roman[i]
        return res
        
sol = Solution()
num = 3
print(sol.intToRoman(num))