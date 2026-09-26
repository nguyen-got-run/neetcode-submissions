class Solution:
    def isValid(self, s: str) -> bool:
        openStack = []
        openChars = set(['(', '[', '{'])
        openToCloseCharDict = {'(': ')', '[': ']', '{': '}'}
        # print(openToCloseCharDict)

        for char in s:
            if char in openChars:
                openStack.append(char)
            else:
                if not len(openStack):
                    return False

                lastOpen = openStack.pop()
                corresponding = openToCloseCharDict.get(lastOpen)

                if corresponding != char:
                    return False

        return not bool(len(openStack))
        