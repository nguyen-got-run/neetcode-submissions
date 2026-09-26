class Solution:
    def isPalindrome(self, s: str) -> bool:
        leftI = 0
        rightI = len(s) - 1

        while leftI <= rightI:
            leftCh = s[leftI]
            rightCh = s[rightI]

            if not leftCh.isalnum():
                leftI += 1
                continue
            
            if not rightCh.isalnum():
                rightI -= 1
                continue
            
            if leftCh.lower() != rightCh.lower():
                return False
            
            leftI += 1
            rightI -= 1
        
        return True