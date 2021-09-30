#!/usr/bin/python3
import sys

num = 0
if len(sys.argv) > 2 or len(sys.argv) > 2:
    print("Usage: nqueens N")
    exit(1)
else:
    if type(int(sys.argv[1])) is not int:
        print("N must be a number")
        exit(1)
    else:
        if int(sys.argv[1]) < 4:
            print("N must be at least 4")
            exit(1)
        else:
            num = int(sys.argv[1])


class Solution:
    @staticmethod
    def solvenqueens(n):
        col = set()
        posdiag = set()  # (r + c)
        negdiag = set()  # (r - c)

        res1 = []
        board = [["."] * n for i in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row1) for row1 in board]
                res1.append(copy)
                return
            for c in range(n):
                if c in col or (r + c) in posdiag or (r - c) in negdiag:
                    continue

                col.add(c)
                posdiag.add(r + c)
                negdiag.add(r - c)
                board[r][c] = "Q"

                backtrack(r + 1)

                col.remove(c)
                posdiag.remove(r + c)
                negdiag.remove(r - c)
                board[r][c] = "."
        backtrack(0)
        return res1


result = Solution()
result = result.solvenqueens(num)
res = []
for r1 in result:
    d = []
    for s in range(len(r1)):
        for c1 in range(len(r1[s])):
            if r1[s][c1] == "Q":
                d.append([s, c1])
    res.append(d)
for row2 in res:
    print(row2)
