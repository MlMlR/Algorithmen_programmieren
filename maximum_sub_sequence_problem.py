import random
import time as t
import math 

input = [31, -41, 59, 26, -53, 58, 97, -93, -23]

def alg1(list):
    ll =len(list)
    si = 0
    ei = 0
    max_win = 0
    for i in range(ll):
        for j in range(i, ll):
            if sum(list[i:j+1]) > max_win:
                max_win = sum(list[i:j+1])
    print(max_win)
    
    
def list_comprehention(list):
    print(max([0] + [sum(list[s:e + 1]) for s in range(len(list)) for e in range(s, len(list))]))


if __name__ == '__main__':
    for i in range(5):
        sample = [random.randint(-100, 100) for _ in range(9*2**i)]
        print (9*2**i)
        start = t.time()
        list_comprehention(sample)
        end = t.time()
        print(end-start)