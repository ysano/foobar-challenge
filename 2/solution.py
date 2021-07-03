#!/usr/bin/env python3.7
def solution(xs):
    # Your code here
    import functools
    from decimal import Decimal

    negatives = list(filter(lambda x: x < 0, xs))

    if len(xs) == 1 and len(negatives) == 1: # case [-10]
        print("{:.0f}".format(xs.pop(0)))
        return

    if len(negatives) % 2 == 1:
        use_negatives = sorted(negatives)[:len(negatives)-1]
    else:
        use_negatives = negatives # even negatives

    use_positives = list(filter(lambda x: x > 0, xs))

    uses = use_positives + use_negatives
    print(uses)

    uses = list(filter(lambda x: x > 1 or x < -1, uses))
    print(uses)

    # if len(uses) == len(xs):
    #     uses = list(map(lambda x: abs(x), uses))
    #     uses.remove(min(uses))

    if len(uses) > 1:
        res = functools.reduce(lambda x,y: Decimal(str(x)) * Decimal(str(y)), uses)
    else:
        if len(uses) == 0:      # case: [-10, 0]
            res = 0
        else:
            res = uses.pop(0)
    print("{:.0f}".format(res))
    

if __name__ == "__main__":

    """
    array: 1-50 panels
    pwoer out level: no greater than 1000

    """
    # test 0
    solution([2,-3,1,0,-5])     # 30
    """
    maximum product found
    xs[0] = 2, xs[1] = -3, xs[4] = -5
    2*(-3)*(-5) = 30
    """

    # test 1
    solution([2, 0, 2, 2, 0]) # 8

    # test 2
    solution([-2, -3, 4, -5]) # 60

    # original
    solution([0.5, 1, 2, 10])   # 20

    # original
    solution([10])   # 10

    # original
    solution([-10])   # -10

    # original
    solution([-10, 0])   # 0
    
    # original
    solution([1000 for f in range(50)])   # 1000**50
    
    # original
    solution([100000000,200000000,300000000])   # 
    
    # original
    solution([5, 4, 2, 10])   # 200


