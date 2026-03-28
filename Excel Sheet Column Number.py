class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for i in columnTitle:
            a = ord(i) - ord("A") + 1
            result = result * 26 + a
        return result