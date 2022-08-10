def aaa (a,b,c):
    return a+b-c

y=aaa(2,3,4)

def zzz (x,a,b,c):
    c=c+1
    print(x,a,b,c)
    t=b(a,c,x)
    return t
z=zzz(1,2,aaa,3)
print(z)

