"""Nearer"""
def main():
    """function"""
    num_alice = int(input())
    num_bob = int(input())
    num_ice = int(input())
    if abs(num_alice - num_ice) < abs(num_bob - num_ice):
        print("Alice %d" %(abs(num_alice - num_ice)))
    elif abs(num_alice - num_ice) > abs(num_bob - num_ice):
        print("Bob %d" %(abs(num_bob - num_ice)))
    else:
        print("Sundaes %d" %(abs(num_alice - num_ice)))
main()
