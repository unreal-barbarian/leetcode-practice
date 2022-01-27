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
        self.backtrack(n, [], set(range(n)), set(), set())
        output = self.format_result()
        self.__init__()
        return output

    def v_mirror(self, solution):
        mirror_x = []
        for i, j in solution:
            mirror_x.append((self.n - i - 1, j))
        return frozenset(mirror_x)

    def h_mirror(self, solution):
        mirror_x = []
        for i, j in solution:
            mirror_x.append((i, self.n - j - 1))
        return frozenset(mirror_x)

    def d1_mirror(self, solution):
        mirror_x = []
        for i, j in solution:
            mirror_x.append((j, i))
        return frozenset(mirror_x)

    def d2_mirror(self, solution):
        mirror_x = []
        for i, j in solution:
            mirror_x.append((self.n - j - 1, self.n - i - 1))
        return frozenset(mirror_x)

    def copysolution(self, solution):
        # one solution can copy to 8 solutions!
        v = self.v_mirror(solution)
        h = self.h_mirror(solution)
        d1 = self.d1_mirror(solution)
        d2 = self.d2_mirror(solution)
        hd2 = self.d2_mirror(h)
        vd2 = self.d2_mirror(v)
        d12 = self.d2_mirror(d1)
        self.answer.update([v, h, d1, d2, hd2, vd2, d12])

    def backtrack(self, n, tried, col_set, diag_set1, diag_set2):
        if n == 0:
            solution = frozenset(tried)
            if solution not in self.answer:
                self.answer.add(solution)
                self.copysolution(solution)
        # each row can have one and only one queen!
        # If loop for all rows, it is not necessary and n times slower
        i = 0 if len(tried) == 0 else tried[-1][0] + 1
        # search for column only
        if i == 0:
            # because one solution can be copied to 8 solutions, search of only first half, exclude all tried locations
            real_col_set = set(range(self.n // 2 + self.n % 2))
        else:
            real_col_set = col_set
        for j in real_col_set:
            if not (i + j) in diag_set1 and not (i - j) in diag_set2:
                new_col_set = set(col_set)
                new_col_set.remove(j)
                new_diag_set1 = set(diag_set1)
                new_diag_set2 = set(diag_set2)
                new_diag_set1.add(i + j)
                new_diag_set2.add(i - j)
                self.backtrack(n - 1, tried + [(i, j)], new_col_set, new_diag_set1, new_diag_set2)

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
ans = a.solveNQueens(11)
tb = time.time()
print(tb - ta)
# print(ans)
print(len(ans))
