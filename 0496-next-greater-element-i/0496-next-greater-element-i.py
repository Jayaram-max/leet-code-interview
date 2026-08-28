class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        greater = {}

        for num in nums2:
            while stack and stack[-1] < num:
                greater[stack.pop()] = num

            stack.append(num)

        answer = []

        for num in nums1:
            answer.append(greater.get(num, -1))

        return answer