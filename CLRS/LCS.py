def findLCS(A, n, B, m):
        # write code here
        c = [([0] * (m + 1)) for _ in xrange(n + 1)]
        for i in xrange(n):
            for j in xrange(m):
                if A[i] == B[j]:
                    c[i + 1][j + 1] = c[i][j] + 1
                elif c[i][j + 1] > c[i + 1][j]:
                    c[i + 1][j + 1] = c[i][j + 1]
                else:
                    c[i + 1][j + 1] = c[i + 1][j]
        return c[n][m]


print findLCS("1A2C3D4B56",10,"B1D23CA45B6A",12)
