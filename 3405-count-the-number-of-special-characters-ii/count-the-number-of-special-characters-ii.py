class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower = {}
        upper = {}

        for i, ch in enumerate(word):
            if ch.islower():
                lower[ch] = i
            else:
                upper[ch.lower()] = min(
                    upper.get(ch.lower(), float('inf')),
                    i
                )

        ans = 0

        for ch in lower:
            if ch in upper and lower[ch] < upper[ch]:
                ans += 1

        return ans