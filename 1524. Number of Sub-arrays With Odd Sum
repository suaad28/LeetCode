class Solution(object):
    def numOfSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        count = 0
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                subarray_sum = sum(arr[i:j+1])
                if subarray_sum % 2 != 0:
                    count += 1
        return count
