class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        #Create a list of words in the string
        #Default separator is whitespace

        words = s.split() 

        if not words: #If list is empty
            return 0
        else:
            return len(words[-1])

