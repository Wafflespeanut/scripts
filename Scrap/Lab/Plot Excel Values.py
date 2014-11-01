from pylab import *

def get(s):
    a=[]; print "Enter {}...".format(s)
    while True:
        try:
            g=raw_input()
            if g=="": break
            a.append(float(g))
        except ValueError: return None
    return a

def output():
    X=get('X'); Y1=get('Y1'); Y2=get('Y2');
    figure(figsize=(10,6),dpi=80)
    plot(X,Y1,color="blue",linewidth=2.5,linestyle="-",label="Label-1")
    plot(X,Y2,color="red",linewidth=2.5,linestyle="--",label="Label-2")
    legend(loc='upper left')
    show()
