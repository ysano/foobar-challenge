#!/usr/bin/env python
def solution(n):                # 5/5 pass
    # Your code here
    n = int(n)
    count = 0
    
    if n == 0:
        return 1
        
    while n != 1:
        if n % 2 != 0:
            if n % 4 == 1 or n == 3:
                n -= 1
            else:
                n += 1
        else:
            n //= 2
        count += 1
    return count
    
if __name__ == "__main__":

    print(solution('15'))              # 5 (15 16 8 4 2 1)
    print(solution('4'))               # 2 (4 2 1)

    # original
    print(solution('16'))            # 4
    print(solution('57'))            # 8
    print(solution('73'))            # 9
    # print(solution('17'))
    # print(solution('18'))
    # print(solution('19'))
    # print(solution('20'))
    # print(solution('121'))
    # print(solution(121 * 211 * 3))

    digit309 = ''.join(['9' for i in range(309)])
    # print(digit309)
    # print(solution(digit309))


    
    """
    15 !16 8 4 2 1              # not x7
    15 !14 7 6 3 2 1
    17 !18 9 10 5 6 3 4 2 1
    17 !16 8 4 2 1              # not x3
    20 10 5 !6 3 4 2 1
    20 10 5 !4 2 1              # not x3
    121 122 61 62 31
    121 120 60 30 15 14 7
    121 120 60 30 16 8 4 2 1

    not xprime = n % prime == 0
    """
