#!/usr/bin/env python
def solution(l):
    # Your code here
    # l: list of pos int, length: 2-2000
    # (li,lj,kl) i<j<k
    # l element: 1-999999
    # return: 32bit int, nothing triple=0
    """
    (lx,ly,lz)
    fm = find multiples from left of ly
    fd = find dividers from right of ly
    combination: len(fm) * len(fd)
    search from entire l
    """
    def find_multiples(l, index):
        cur = l[index]
        # print("fm:",l,index,cur, [item for item in l[index + 1:] if item % cur == 0])
        return [item for item in l[index + 1:] if item % cur == 0]

    def find_dividers(l, index):
        cur = l[index]
        # print("fd:",l,index,cur, [item for item in l[:index] if cur % item == 0])
        return [item for item in l[:index] if cur % item == 0]

    list_size = len(l)
    count = 0
    while list_size >= 2:
        list_size -= 1
        count += len(find_dividers(l, list_size)) * len(
            find_multiples(l, list_size))

    return count


if __name__ == "__main__":

    print(solution([1, 2, 3, 4, 5, 6]))  # 3

    print(solution([1, 1, 1]))  # 1

    # original
    print(solution([1, 1]))  # 0

    print(solution([6, 5, 4, 3, 2, 1]))  # 0
    # solution([i for i in range(1,2001)])

    import cProfile
    # cProfile.run('solution([i for i in range(1,2001)])')
