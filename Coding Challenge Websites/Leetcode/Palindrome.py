# Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/submissions/
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # s = "".join(c for c in s if c not in ('!','.',':', ',', '@'))        

        s = re.sub(r'[^A-Za-z0-9 ]+', '', s)
        s = s.replace(' ', '')
        s = s.lower()
        
        
        print(s)
        
        if s == s[::-1]:
            return True
        
        
        
