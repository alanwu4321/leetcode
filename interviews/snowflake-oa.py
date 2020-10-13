import math
import os
import random
import re
import sys
#
# Complete the 'largestArea' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY samples as parameter.
#


def largestArea(samples):

    # Write your code here
    n = len(samples)
    diag = [[0 for x in range(n)] for y in range(n)]
    up = diag
    left = diag

    ret = 0

    for i in range(n):
        for j in range(n):
            if (samples[i][j]):
                diag[i][j] = 1
                up[i][j] = 1
                left[i][j] = 1

                if (i == 0):
                    up[i][j] = 1
                else:
                    up[i][j] = up[i-1][j] + 1

                if (j == 0):
                    left[i][j] = 1
                else:
                    left[i][j] = left[i][j-1] + 1

                if ((i == 0) or (j == 0)):
                    diag[i][j] = 1
                else:
                    diag[i][j] = min(up[i][j], left[i][j], diag[i-1][j-1]+1)

                ret = max(ret, diag[i][j])
            else:
                diag[i][j] = 0
                up[i][j] = 0
                left[i][j] = 0

    return ret


if __name__ == '__main__':

    test = [[1, 1, 1], [1, 1, 0], [0, 1, 1]]

    ans = largestArea(test)
    print(ans)

    test = [[0, 1, 1], [1, 1, 0], [1, 0, 1]]

    ans = largestArea(test)
    print(ans)
