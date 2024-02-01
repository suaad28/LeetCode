class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        record = []
        record_sum = 0

        for i in operations:   
            if i.isnumeric() or (i[0]=='-'): #checking for - for negative ints
                record.append(int(i))
            elif i=="C":
                record.pop()
            elif i=="D":
                record.append(record[-1]*2)
            elif i=="+":
                record.append(record[-1]+record[-2])

        record_sum += sum(record)
        return record_sum

