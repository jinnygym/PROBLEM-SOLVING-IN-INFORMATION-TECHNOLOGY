"""Triangle"""
def main():
    "main"
    num = int(input())          #input = 5
    for i in range(1, num+1):   #1,2,3,4,5
        print(' ' * ((num*2)-(2*i)), end='')   #white_space
        if i == 1:          #Peak point
            print('%02d' % (num-(i-1)))       #number  ex: (5-(i-1));
        else:               #i == 2,3,4,5
            print('%02d' % (num-(i-1)), end='') #number
            print(' ' * (2+(4*(i-2))), end='')  #middle space
            print('%02d' % (num-(i-1)))         #number
main()
