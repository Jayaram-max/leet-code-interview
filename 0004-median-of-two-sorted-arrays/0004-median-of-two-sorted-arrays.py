class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        low, high = 0, m
        total_left = (m + n + 1) // 2
        
        while low <= high:
            mid1 = (low + high) // 2
            mid2 = total_left - mid1
            
            l1 = nums1[mid1 - 1] if mid1 > 0 else float('-inf')
            l2 = nums2[mid2 - 1] if mid2 > 0 else float('-inf')
            r1 = nums1[mid1] if mid1 < m else float('inf')
            r2 = nums2[mid2] if mid2 < n else float('inf')
            
            if l1 <= r2 and l2 <= r1:
                if (m + n) % 2 == 1:
                    return float(max(l1, l2))
                return (max(l1, l2) + min(r1, r2)) / 2.0
            elif l1 > r2:
                high = mid1 - 1
            else:
                low = mid1 + 1
