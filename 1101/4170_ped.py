""" 4170 - PedPonFire """
def main():
    """ Return how many possible pair(s) to match the number with sum """
    lst, cnt, lim = sorted([int(input()) for _ in range(int(input()))]), 0, int(input())
    set_lst = sorted(set(lst))
    for i in set_lst:
        if i > lim//2:
            break
        cnt += lst.count(lim-i)*lst.count(i)
    return cnt
print(main())
