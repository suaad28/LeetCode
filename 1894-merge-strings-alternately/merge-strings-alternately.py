class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        merged = ""
        i = 0
        j = 0
        while i < len(word1) and j < len(word2):
            merged += word1[i]
            merged += word2[j]
            i+=1
            j+=1
        
        merged += word1[i:]
        merged += word2[j:]
        return merged