class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters_available = {}
        for symbol in magazine:
            try:
                letters_available[symbol] += 1
            except:
                letters_available[symbol] = 1
        for letter in ransomNote:
            try:
                letters_available[letter] -= 1
            except:
                return False

        for number in letters_available.values():
            if number < 0:
                return False
        return True


case1 = Solution()

print(case1.canConstruct("aab", "aabb"))


print(case1.canConstruct("aab", "abb"))

