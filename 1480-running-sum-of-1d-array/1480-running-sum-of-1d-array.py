class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix =[0]
        for x in nums :
            prefix.append(prefix[-1]+x)
        return prefix [1:]