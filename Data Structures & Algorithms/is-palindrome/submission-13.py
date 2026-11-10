class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_joined = (''.join(s)).lower()
        onlychar = ''
        for char in s_joined:
            if char.isalnum():
                onlychar += char
        left = 0
        right = len(onlychar) - 1
        while left < right:
            if onlychar[left] == onlychar[right]:
                left += 1
                right -= 1
            else:
                return False
        return True