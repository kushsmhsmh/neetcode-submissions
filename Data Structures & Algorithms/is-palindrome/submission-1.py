class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s1 = ""
        for ch in s:
            if ch.isalpha() or ch.isdigit():
                s1 += ch
        if s1 == s1[::-1]:
            return True
        else:
            return False