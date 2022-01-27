import time
class Solution(object):
    def __init__(self):
        self.answer = set()
        self.n = 0

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.n = n
        self.answer = self.backtrack(n, [], set(range(n)), set(), set())
        output = self.format_result()
        self.__init__()
        return output

    def backtrack(self, n, tried, col_set, diag_set1, diag_set2):
        if n == 0:
            return [tried]
        solution = []
        for i in range(0 if len(tried) == 0 else tried[-1][0] + 1, self.n):
            for j in col_set:
                if not (i + j) in diag_set1 and not (i - j) in diag_set2:
                    new_col_set = set(col_set)
                    new_col_set.remove(j)
                    new_diag_set1 = set(diag_set1)
                    new_diag_set2 = set(diag_set2)
                    new_diag_set1.add(i+j)
                    new_diag_set2.add(i-j)
                    solution += self.backtrack(n - 1, tried + [(i, j)], new_col_set, new_diag_set1, new_diag_set2)
        return solution

    def format_result(self):
        output = []
        for solution in self.answer:
            board = [[0] * self.n for i in range(self.n)]
            for i, j in solution:
                board[i][j] = 1
            output.append([''.join(["Q" if j > 0 else "." for j in row]) for row in board])
        return output


a = Solution()
# a.answer = {frozenset({(2,3)})}
# a.n = 4
# print(a.format_result())
ta = time.time()
ans = a.solveNQueens(9)
tb = time.time()
print(tb-ta)
print(ans)
print(len(ans))
