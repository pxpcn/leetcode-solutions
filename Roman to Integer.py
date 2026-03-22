class Solution:
    def romanToInt(self, s: str) -> int:
        Roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        count = 0
        for i in range(len(s)):
            if i + 1 < len(s) and Roman[s[i]] < Roman[s[i + 1]]:
                count -= Roman[s[i]]
            else:
                count += Roman[s[i]]
        return count

        