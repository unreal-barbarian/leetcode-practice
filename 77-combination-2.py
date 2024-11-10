def combine(n: int, k: int):
    trace = []
    result = []

    def bt(pt):
        if len(trace) == k:
            result.append(trace[:])
            return
        else:
            for i in range(pt, n - k + pt + 1):
                trace.append(i)
                bt(pt+1)
                trace.pop()
    bt(1)
    return result
print(combine(4,2))
