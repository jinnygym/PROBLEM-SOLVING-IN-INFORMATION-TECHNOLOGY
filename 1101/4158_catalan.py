""" 4158 - Catalan """
def main():
    """ Catalan """
    pos, cur = int(input()), 1
    for i in range(1, pos):
        cur = (((4*i)+2)/(i+2))*cur
    print(int(cur))
main()
