class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = ""
        for char in s : 
            if char.isalnum() : 
                word += char

        return word.lower() == word.lower()[::-1]