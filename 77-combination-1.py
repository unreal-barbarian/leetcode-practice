def combine(n: int, k: int):
    if n < k:
        return []
    if n == k:
        return [list(range(1, n + 1))]
    track = [1] * k
    res = []
    i = 1

    def back(ii):
        if track[ii - 1] < n - k + ii:
            track[ii - 1] += 1
            return ii
        else:
            ii = ii - 1
            if ii == 0:
                return 0
            else:
                return back(ii)

    while True:
        if i == k:
            res.append(track[:])
            i = back(i)
            if i == 0:
                return res
        else:
            track[i] = track[i - 1] + 1
            i += 1


print(combine(5, 3))
