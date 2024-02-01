class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        i = 0
        x = sorted(arr)

        #setting the reference difference for the sequence
        diff = (x[i+1] - x[i])  

        for i in range(1,len(x)-1):
            if (x[i+1] - x[i]) != diff:
                return False
        return True

