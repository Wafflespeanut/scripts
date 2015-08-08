def powersum(n, r):
    a = 0
    for i in range(2, r + 1):
        l, s = i, 0
        while l != 0:
            s += int(l % 10) ** n
            l /= 10
        if s == i:
            a += i
    return a

# n, r = 5, 200000
# print "The sum of all numbers that can be written as sum of nth powers of their digits: " + str(powersum(n, r))
