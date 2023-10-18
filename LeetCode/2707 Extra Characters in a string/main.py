class Solution:
    def minExtraChar(self, s: str, dictionary: list[str]) -> int:
        dictionary.sort(key=len)
        dictionary.reverse()
        print(dictionary)
        for slowo in dictionary:
            indx = s.find(slowo)
            while indx != -1:
                word = [a for a in s]
                for _ in range(len(slowo)):
                    word.pop(indx)
                s = "".join(word)
                indx = s.find(slowo)
        return len(s)


ll = Solution()
print(ll.minExtraChar("azvzulhlwxwobowijiyebeaskecvtjqwkmaqnvnaomaqnvf",
["na","i","edd","wobow","kecv","b","n","or","jj","zul","vk","yeb","qnfac","azv","grtjba","yswmjn","xowio","u","xi","pcmatm","maqnv"]))