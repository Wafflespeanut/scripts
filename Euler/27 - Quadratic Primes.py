execfile("7 - 10001st Prime.py")

def check(a,b):
    n=0; m=0
    while True:
        m=n**2+a*n+b
        if m not in plist: break
        n+=1
    if n>1: return [n,m]
    else: return False

def prange(r):
    gen=sieve(r); final=[1]
    for i in gen: final.append(-i); final.append(i)
    return final

def gen(r):
    prg=prange(r); t=0; m=[0,0]; found=[]
    for a in prg:
        for b in sieve(r):  # All integers are not necessary
            if check(a,b):
                m=check(a,b)
                if m[0]>t: t=m[0]; found=[a,b]
    return found

#plist=sieve(100000); f=gen(1000); print "The coefficients " +str(f)+ " produce the maximum number of primes for consecutive 'n'\n\nProduct of the coefficients: " +str(f[0]*f[1])
