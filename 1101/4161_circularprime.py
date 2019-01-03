""" 4161 - CircularPrime """
def isprime(num, cnt=0):
    """ Check for prime number """
    if num <= 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if not num%i:
            cnt = 1
            break
    return False if cnt else True
def iscprime(num):
    """ Check for circular prime """
    num = str(num)
    for _ in range(len(num)):
        num = con = num[1:] + num[0]
        if not isprime(int(con)):
            return False
    return True
def main(cnt=0):
    """ Main """
    num = int(input())
    for i in range(1, num+1):
        cnt += i if iscprime(i) else 0
    print(cnt)
main()
