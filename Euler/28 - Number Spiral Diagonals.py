def spiral(n):
    c=1; diag=1; i=1
    while i<n**2:
        r=1
        while r<=4:
            if c%2==1: i+=c+1; diag+=i
            r+=1
        c+=1
    return diag

n=1001; s=spiral(n)            
print "The sum of diagonal numbers in a " +str(n)+ " by " +str(n)+ " spiral is: " +str(s)
