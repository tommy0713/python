def aaa (a,b,c):
    return a+b-c

y=aaa(2,3,4)

def zzz (x,a,b,c):
    c=c+1
    print(x,a,b,c)
    t=x(a,b,c)
    return t
z=zzz(aaa,1,2,3)
print(z)

