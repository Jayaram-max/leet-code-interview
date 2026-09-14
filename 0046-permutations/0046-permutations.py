class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        result = []

        def backtrack(current, rem):
            if not rem:
                result.append(current[:])
                return

            for i in range(len(rem)):
                current.append(rem[i])
                backtrack(current, rem[:i] + rem[i+1:])
                current.pop()

        backtrack([], nums)

        return result