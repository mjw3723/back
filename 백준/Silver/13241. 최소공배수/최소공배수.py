import sys
import math
input = sys.stdin.readline

N, M = map(int, input().split())
SHIFT = 30
MASK = (2 ** SHIFT)

def split_number(bignum):
    t = abs(bignum)
    num_list = []
    while t != 0:
        small_int = t % MASK
        num_list.append(small_int)
        t = t // MASK
    return num_list

def restore_number(num_list):
    bignum = 0
    for i, n in enumerate(num_list):
        bignum += n * (2 ** (SHIFT * i))
    return bignum

gcd_value = math.gcd(N, M)
lcm_value = (abs(N) // gcd_value) * abs(M)

num_list = split_number(lcm_value)
restored_lcm = restore_number(num_list)

print(restored_lcm)