"""Restaurant"""
def main(num1, num2, num3, num4):
    """code"""
    price = num1 + num4
    per = price - (price * num3/100)
    per2 = num1 - (num1 * num3/100)
    if num1 == per or per == per2:
        print("Yes")
    elif num1 == num2:
        print("No %.3f" %(per - per2))
    elif num1 > per:
        print("Yes %.3f" %(num1 - per))
    else:
        print("No %.3f" %(per - num1))
main(float(input()), float(input()), float(input()), float(input()))
