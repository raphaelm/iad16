def quicksort(seq, key=lambda s: s):
    """
    Iteratives QuickSort entsprechend Skript Seite 39
    """
    stack = []
    n = len(seq)
    stack.append(0)
    stack.append(n - 1)

    while stack:
        r, l = stack.pop(), stack.pop()
        if l < r:
            v = key(seq[r])
            i = l - 1
            j = r
            while True:
                while True:
                    i += 1
                    if i >= n or key(seq[i]) >= v:
                        break
                while True:
                    j -= 1
                    if j < 0 or key(seq[j]) <= v:
                        break
                if j > i:
                    seq[i], seq[j] = seq[j], seq[i]
                else:
                    seq[i], seq[r] = seq[r], seq[i]
                    break
            if i - 1 <= r - i:
                stack.append(i+1)
                stack.append(r)
                stack.append(l)
                stack.append(i-1)
            else:
                stack.append(l)
                stack.append(i-1)
                stack.append(i+1)
                stack.append(r)
    return seq