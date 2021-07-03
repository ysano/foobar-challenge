#!/usr/bin/env python3.7
def solution1(data,n):
    # Your code here
    if len(data) >= 100:
        raise ValueError
    res = []
    uniqs = list(set(data))
    for u in uniqs:
        if data.count(u) <= n:
            res.append(u)
    print(",".join([str(r) for r in res]))
    """
Verifying solution...
Test 1 passed!
Test 2 passed!
Test 3 passed! [Hidden]
Test 4 passed! [Hidden]
Test 5 failed  [Hidden]
Test 6 passed! [Hidden]
Test 7 failed  [Hidden]
Test 8 passed! [Hidden]
Test 9 failed  [Hidden]
    """
    
def solution(data,n):
    # Your code here
    res = []
    already_removed = {}
    for d in data:
        res.append(d)
        if res.count(d) > n or already_removed.get(d):
            res = list(filter(lambda x: x != d, res))
            already_removed[d] = True;
        # print("already_removed: ",already_removed)
        # print("res: ",res)

    print(",".join([str(r) for r in res]))
    
if __name__ == "__main__":

    # test 1
    solution([1, 2, 3], 0)

    # test 2
    solution([1, 2, 2, 3, 3, 3, 4, 5, 5], 1)

    # original
    # solution([1, 2, 3, 2, 2, 3, 3, 4, 2, 2, 5, 5], 3)

    # original
    # solution([n for n in range(99)], 10)
    
    """
    dataの要素の個数がn個のものを探す
    """

