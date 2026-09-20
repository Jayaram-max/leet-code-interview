class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}

        for x in nums:
            count[x] = count.get (x, 0) + 1

        res = sorted(count,key=count.get,reverse=True)
        return res[:k]