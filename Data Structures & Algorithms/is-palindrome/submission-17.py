class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        new_str = ''
        for c in s:
            if c.isalnum():
                new_str += c
        i = 0
        j = len(new_str) - 1
        while i < j:
            if new_str[i] == new_str[j]:
                i += 1
                j -= 1
            else:
                return False
        return True

        