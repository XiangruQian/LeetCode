class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        if A == '':
            return -1
        cnt = int(len(B) / len(A))
        if cnt * len(A) < len(B):
            cnt += 1
        C = A * (cnt + 1)
        for i in range(len(A)):
            if C[i:i + len(B)] == B:
                if i + len(B) <= len(C) - len(A):
                    return cnt
                else:
                    return cnt + 1
        return -1