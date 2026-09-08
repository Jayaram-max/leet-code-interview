class Solution:
    def searchInsert(self, s: List[int], target: int) -> int:
        l = 0
        r = len(s) - 1 
        while l <= r:
            mid = (l + r) // 2
            if s[mid] == target:
                return mid 
            elif s[mid] <  target :
                l = mid +1 
            else :
                r = mid -1 
        return l
         
