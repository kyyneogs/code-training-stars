#efficient way

def s(n):
    if n==1:return ['*']

    T=s(n-1)[::-1]
    L=len(T)
    A=[]
    
    A.append(' '*(2*L)+'*'+' '*(2*L))
    for i in range(1,L):A.append(' '*(2*L-i)+'*'+' '*(2*i-1)+'*'+' '*(2*L-i))
    for i in range(L):A.append(' '*(L-i)+'*'+' '*i+T[i]+' '*i+'*'+' '*(L-i))
    A.append('*'*(4*L+1))
    return A

N=int(input())
ans=s(N)
a,b=len(ans[0]),len(ans)
for i in range(len(ans)):ans[i]=ans[i][:a-b+1+i]
print('\n'.join(ans[::-1]) if N%2==0 else '\n'.join(ans))