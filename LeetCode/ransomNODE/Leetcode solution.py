import collections


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return collections.Counter(ransomNote) <= collections.Counter(magazine)


case1 = Solution()

print(case1.canConstruct("aab", "abb"))
