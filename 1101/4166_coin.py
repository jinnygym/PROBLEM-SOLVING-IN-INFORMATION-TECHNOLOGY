""" 4166 - CoinChangeV1 """
def main(mny, cnt=0):
    """ Coin """
    for i in (25, 10, 5, 1):
        cnt += mny//i
        mny -= (mny//i)*i
    print(cnt)
main(int(input()))
