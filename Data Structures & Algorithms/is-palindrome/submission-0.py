class Solution:
    def isAlphanumeric(self, char: str) -> bool:
        asc = ord(char)
        zero = ord('0')
        nine = ord('9')
        a = ord('A')
        z = ord('z')

        return zero <= asc <= nine or a <= asc <= z

    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left <= right:
            lChar = s[left]
            rChar = s[right]
            doSkip = False

            if not self.isAlphanumeric(lChar):
                left += 1
                doSkip = True
            
            if not self.isAlphanumeric(rChar):
                right -= 1
                doSkip = True
            
            if doSkip:
                continue
            
            lAsc = ord(lChar.lower())
            rAsc = ord(rChar.lower())

            if lAsc != rAsc:
                return False
            else:
                left += 1
                right -= 1
        
        return True