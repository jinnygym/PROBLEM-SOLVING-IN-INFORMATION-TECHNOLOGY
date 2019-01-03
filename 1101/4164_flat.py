""" 4164 - Flatten """
import json
def main(ilst):
    """ Flatten list """
    def islist(i):
        """ Check if 'i' is the list or not if not convert it"""
        for j in i:
            if isinstance(j, list):
                islist(j)
            else: ilst.append(j)
    islist(json.loads(input()))
    print(sorted(ilst, reverse=True))
main([])
