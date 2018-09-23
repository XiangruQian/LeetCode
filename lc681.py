class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        digits = {int(time[0]),int(time[1]),int(time[3]),int(time[4])}
        h = int(time[0:2])
        m = int(time[3:5])
        while True:
            m += 1
            if m == 60:
                h, m = (h + 1) % 24, 0
            if {h%10, int(h/10), m%10, int(m/10)}.issubset(digits):
                return str(int(h/10)) + str(h%10) + ':' + str(int(m/10)) + str(m%10)


a = Solution()
print(a.nextClosestTime("20:48"))