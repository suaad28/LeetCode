class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        listed = []

        #convert the list to a number
        number = int(''.join(str(i) for i in digits))
        number +=1
        st = str(number)

        #turn it back to a list
        listed.extend(int(i) for i in st)

        return listed
        
        