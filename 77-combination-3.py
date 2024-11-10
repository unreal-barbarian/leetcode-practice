def combine(n: int, k: int):
    if n < k:
        return []
    if n == k:
        return [list(range(1, n + 1))]
    track = list(range(1, k + 1))
    result = [track[:]]
    i = k - 1

    while True:
        if i == -1:
            break
        if track[i] < n - k + i + 1:
            track[i] += 1
            track[i + 1:] = list(range(track[i] + 1, track[i] + k - i))
            i = k - 1
            result.append(track[:])
        else:
            i -= 1
    return result


print(combine(5, 3))
