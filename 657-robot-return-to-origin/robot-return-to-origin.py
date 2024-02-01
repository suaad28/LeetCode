class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        lr = 0
        ud = 0

        #setting opposite directions with corresponding opposite signs
        for i in moves:
            if i == 'L':
                lr +=1
            if i == 'R':
                lr -=1
            if i == 'U':
                ud +=1
            if i == 'D':
                ud -=1

        if abs(lr) > 0 or abs(ud) > 0:
            return False
        else:
            return True