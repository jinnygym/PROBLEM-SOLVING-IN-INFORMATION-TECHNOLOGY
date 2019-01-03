""" 4159 - Day2011 """
def main():
    """ Return day corresponding to entered date in 2011 """
    day, mth = int(input()), int(input())
    mths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    wks = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    yrday = sum(mths[:mth-1])+day
    cur_idx = 0
    for _ in range(yrday):
        if cur_idx == 6:
            cur_idx = 0
        else:
            cur_idx += 1
    print(wks[cur_idx-1])
main()
