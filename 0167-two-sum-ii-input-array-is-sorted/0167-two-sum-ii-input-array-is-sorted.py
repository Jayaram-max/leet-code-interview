class Solution:
    def twoSum(self,  s : List[int], target: int) -> List[int]:
        l = 0
        r = len(s) - 1

        while l < r :
            total = s[l] + s[r]

            if total == target:
                return [l + 1 , r + 1]
            elif total < target :
                l += 1
            else:
                r -= 1