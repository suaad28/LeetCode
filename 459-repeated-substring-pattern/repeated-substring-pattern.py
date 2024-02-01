class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        length = len(s)

        for i in range(1, (length // 2) + 1):
            substring = s[:i]
            l = len(substring)

            #if the substring * the len(substring) is equal to s
            if substring * (length // l) == s:
                return True
        return False