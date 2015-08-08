def ways(n, stuff):
    ways = [1] + [0 for i in range(n)]
    for i in stuff:
        for j in range(i, n + 1):
            ways[j] += ways[j - i]
    return ways[n]

# n, coins = 200, [1, 2, 5, 10, 20, 50, 100, 200]
# print "There are " + str(ways(n, coins)) + " ways to get to " + str(n) + " pennies!"
