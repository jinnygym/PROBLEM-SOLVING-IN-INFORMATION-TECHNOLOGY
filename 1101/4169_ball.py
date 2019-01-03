""" 4169 - Ball """
def main():
    """ Ball """
    hth = float(input())
    if hth <= 0.01:
        print(0)
        return
    cnt = 0
    while hth > 0.01:
        hth -= hth * 2/5
        cnt += 1
    print(cnt - 1)
main()
