""" 4165 - CaesarV1 """
def main(stp, txt):
    """ Shift then display the given text  """
    for i in txt:
        if 65 <= ord(i.upper()) <= 90:
            if i.isupper():
                print(chr((ord(i)+stp-65)%26+65), end="")
            else: print(chr((ord(i)+stp-97)%26+97), end="")
        else:
            print(i, end="")
main(int(input())%26, input())
