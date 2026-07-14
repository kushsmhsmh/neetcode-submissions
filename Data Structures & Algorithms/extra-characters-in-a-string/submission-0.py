class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i-1]
            for word in dictionary:
                wlen = len(word)

                if i >= wlen:
                    if s[i - wlen : i] == word:
                        dp[i] = max(dp[i], dp[i - wlen] + wlen)
        return n - dp[n]
