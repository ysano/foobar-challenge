#!/usr/bin/env python3.7
def solution(l):
    # Your code here
    def versiongetter(*items):
        if len(items) == 1:
            item = items[0]
            def g(obj):
                return obj[item]
        else:
            def g(obj):
                res = []
                for item in items:
                    try:
                        res.append(int(obj[item]))
                    except IndexError:
                        res.append(-1)
                return tuple(res)
        return g

    l = list(map(lambda x: x.split('.'),l))
    l = sorted(l, key=versiongetter(0,1,2))

    l = list(map(lambda x: ".".join(x),l))
    l = ",".join(l)
    print(l)

if __name__ == "__main__":

    solution(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"])
    # 0.1, 1.1.1, 1.2, 1.2.1, 1.11, 2, 2.0, 2.0.0

    solution(["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"])
    # 1.0, 1.0.2, 1.0.12, 1.1.2, 1.3.3
