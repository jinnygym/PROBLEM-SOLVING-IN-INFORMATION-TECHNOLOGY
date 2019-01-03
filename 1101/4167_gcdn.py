""" 4167 - GCD_N """
def gcd(num_1, num_2):
    """ Find GCD """
    while num_2:
        num_1, num_2 = num_2, num_1%num_2
    return num_1
def main(num):
    """ Find Great Common Divisor of n number(s) """
    if num == 1:
        return int(input())
    mgcd = gcd(int(input()), int(input()))
    for _ in range(2, num):
        mgcd = gcd(mgcd, int(input()))
    return mgcd
print(main(int(input())))
