class Solution:
    def threeSum(self, s: list[int]) -> list[list[int]]:
        s.sort()
        res = []

        for i in range(len(s)):
            if i > 0 and s[i] == s[i - 1]:
                continue

            l = i + 1
            r = len(s) - 1

            while l < r:
                total = s[i] + s[l] + s[r]

                if total == 0:
                    res.append([s[i], s[l], s[r]])

                    while l < r and s[l] == s[l + 1]:
                        l += 1

                    while l < r and s[r] == s[r - 1]:
                        r -= 1

                    l += 1
                    r -= 1

                elif total < 0:
                    l += 1

                else:
                    r -= 1

        return res