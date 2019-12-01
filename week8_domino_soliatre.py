n=int(input())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l=[l1,l2]
a1=[]
a2=[]
for i in range(n):
  a1.append(abs(l[0][i]-l[1][i]))
for i in range(n-1):
  h_p=abs(l[0][i+1]-l[0][i])+abs(l[1][i+1]-l[1][i])
  v_p=a1[i]+a1[i+1]
  a2.append(max(h_p,v_p))
score=[a1[0],a2[0]]
for i in range(2,n):
  m=max((a1[i]+score[i-1]),(a2[i-1]+score[i-2]))
  score.append(m)
print(score[n-1])
