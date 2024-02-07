class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        n = len(mat)
        ans = 0
        for i in range(n):
            ans += mat[i][i]       #Primary Diagonal
            ans += mat[n-1-i][i]   #Secondary Diagonal
        
        if n%2!=0:
            ans -=mat[n//2][n//2]   #Subtracting the repeat

        return ans