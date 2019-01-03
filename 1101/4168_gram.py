""" 4168 - GramV1 """
def main(txt):
    """ Find 2-gram of entered string """
    lst = [txt[i:i+2] for i in range(len(txt))]
    mode = max(lst, key=lst.count)
    print(mode, lst.count(mode), sep="\n")
main(input())
