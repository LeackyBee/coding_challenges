class Solution:
    def romanToInt(self, s: str) -> int:
        if not s:
            return 0
        values = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1
        }
        chars = (('M', 'C'), ('D', 'C'), ('C', 'X'), ('L', 'X'), ('X', 'I'), ('V', 'I'), ('I', ''))
        total = 0
        i = 0
        for main, decrement in chars:
            if i == len(s) - 1:
                total += values[s[i]]
                break

            while i < len(s) and s[i] == main:
                total += values[main]
                i += 1

            if i + 1 < len(s) and s[i + 1] == main:
                total += values[main] - values[decrement]
                i += 2
        return total