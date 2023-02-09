import random
import timeit

input = [31, -41, 59, 26, -53, 58, 97, -93, -23]

def alg1(list):
    ll =len(list)
    si = 0
    ei = 0
    max_win = 0
    for i in range(ll):
        for j in range(i, ll):
            if sum(list[i:j+1]) > max_win:
                si = i
                ei = j
                max_win = sum(list[i:j+1])
    
    print(max([0] + [sum(list[start:end + 1]) for start in range(len(list)) for end in range(start, len(list))]))
    print(si)
    print(ei)
    print(max_win)
    




if __name__ == '__main__':
    alg1(input)