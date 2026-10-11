class Solution:
    def isPalindrome(self, s: str) -> bool:
        word="".join(char.lower() for char in s if char.isalnum())
        reverse=word[::-1]
        return word == reverse 


