x,y=int(input('Introduceti prima fractie: ')),int(input())
q,z=int(input('Introduceti a doua fractie: ')),int(input())
def adunare(a,b,n,m):
    i=((a*m)+(b*n))/(b*m)
    return (i)
print(x,'/',y,'+',q,'/',z,'=',adunare(x,y,q,z),sep='')

def inmultire(a,b,n,m):
    i=(a*n)/(b*m)
    return (i)
print(x,'/',y,'*',q,'/',z,'=',inmultire(x,y,q,z),sep='')

