class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # Using find(), a built-in method for strings to find the 
        #index of the first occurrence of a substring within another string
        # returns -1 by defauly if not found
        # string.find(substr, start, end)
        
        return haystack.find(needle)
            