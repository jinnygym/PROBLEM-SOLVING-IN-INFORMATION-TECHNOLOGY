"""Largest Number"""
def main(nm1, nm2, nm3):
    """compare"""
    n123, n132, n213, n231, n312, n321 = int(nm1+nm2+nm3), int(nm1+nm3+nm2), int(nm2+nm1+nm3) \
    , int(nm2+nm3+nm1), int(nm3+nm1+nm2), int(nm3+nm2+nm1)

    if n123 >= n132 and n123 >= n213 and n123 >= n231 and n123 >= n312 and n123 >= n321:
        print(n123)
    elif n132 >= n123 and n132 >= n213 and n132 >= n231 and n132 >= n312 and n132 >= n321:
        print(n132)
    elif n213 >= n123 and n213 >= n132  and n213 >= n231 and n213 >= n312 and n213 >= n321:
        print(n213)
    elif n231 >= n123 and n231 >= n132 and n231 >= n213 and n231 >= n312 and n231 >= n321:
        print(n231)
    elif n312 >= n123 and n312 >= n132 and n312 >= n213 and n312 >= n231 and n312 >= n321:
        print(n312)
    elif n321 >= n123 and n321 >= n132 and n321 >= n213 and n321 >= n231 and n321 >= n312:
        print(n321)

main(input(), input(), input())
