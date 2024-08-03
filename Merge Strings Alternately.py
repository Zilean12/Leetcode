class Solution(object):
    def mergeAlternately(self, word1, word2):
        merged = ""
        i = 0
        while i < len(word1) and i < len(word2):
            merged += word1[i] + word2[i]
            i += 1
        if i < len(word1):
            merged += word1[i:]
        if i < len(word2):
            merged += word2[i:]
        print("Merged String:", merged)
        return merged

sol = Solution()
word1 = "abc"
word2 = "pqr"
sol.mergeAlternately(word1, word2)
