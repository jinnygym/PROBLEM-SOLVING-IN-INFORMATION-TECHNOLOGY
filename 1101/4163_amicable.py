""" 4164 - Amicable """
def find_pair(num):
    """ Return pair of amicable number """
    res = []
    for i in range(1, num+1):
        j = sum_f(i)
        if sum_f(j) == i and i != j:
            res.append(tuple(sorted((i, j))))
    return sum(map(lambda i: i[0]+i[1], set(res)))
def sum_f(num):
    """ Sum Factors """
    res = []
    for i in range(1, int(num**0.5) + 1):
        if not num%i:
            res.extend([i, num//i])
    return sum(set(res)-set([num]))
print(find_pair(int(input())))
