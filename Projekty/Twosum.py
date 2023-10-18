class Solution:
    @classmethod
    def Twosum(self, target, *nums):
        index = []
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    index.append(i)
                    index.append(j)
                    break
            if(len(index)>0):
                break
        return index
            


print(Solution.Twosum(9, 1, 3, 1, 8))

