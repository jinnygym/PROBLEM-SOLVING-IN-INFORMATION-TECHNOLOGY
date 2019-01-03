"""Milk"""
def main(price, promotion, free, money):
    """How many milk you can get"""
    keep = money//price
    bottles = keep
    if promotion != 0:
        while keep >= promotion:
            get = keep//promotion*free
            keep = keep%promotion + get
            bottles += get
    print(bottles)
main(int(input()), int(input()), int(input()), int(input()))
