# 출처: https://www.hackerrank.com
# problem : lonely integer


# timeout error
def timeout_lonelyinteger(a):
    if len(a) == 1:
        return a[0]
    else:
        a.sort()
        while len(a) > 1:
            if a[0] == a[1]:
                a.pop(0)
                a.pop(0)
        return a[0]


# better approach with recursion
def lonelyinteger(a):
    a = sorted(a)
    if len(a) < 3:
        return a[0]
    elif a[0] != a[1]:
        return a[0]
    else:
        return lonelyinteger(a[2:])


if __name__ == "__main__":
    a = int(input())
    b = map(int, input().strip().split(" "))
    print(lonelyinteger(b))
