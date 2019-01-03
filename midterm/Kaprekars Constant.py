"""Kaprekar's Constant"""
def main(num, count):
    """result = 6174"""
    while num != '6174':
        snum = ''
        for i in range(9, -1, -1):
            if str(i) in num:
                snum += str(i)*(num.count(str(i)))
        high, lower = snum, snum[::-1]
        num = "%04d" % (int(high) - int(lower))
        count += 1
    print(count)
main(input(), 0)


