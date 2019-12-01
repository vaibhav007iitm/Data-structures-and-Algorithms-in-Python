def frequency(l):
	sl=l[:]
	sl.sort()
	sl=sl+[sl[len(l)-1]+1]
	min_f=[]
	max_f=[]
	mnf=len(l)
	mxf=0
	f=1
	#print(sl,l)
	for i in range(len(l)):
		if sl[i]==sl[i+1]:
			f=f+1
		else:
			if f<mnf:
				(min_f,mnf)=([sl[i]],f)
			elif f==mnf:
				min_f.append(sl[i])
			if f>mxf:
				(max_f,mxf)=([sl[i]],f)
			elif f==mxf:
				max_f.append(sl[i])
			#print(sl[i],f)
			f=1
	return ((min_f,max_f))
from bisect import bisect_left
def onehop(l):
	s=sorted(l)
	ref=[s[i][0] for i in range(len(l))]
	#print(ref)
	ans=[]
	for i in range(len(l)):
		x=s[i][1]
		p=bisect_left(ref,x)
		if p>=len(l) or p<0:
			continue
		#print(p)
		while p<len(l) and x==ref[p]:
			(e,j)=(s[i][0],s[p][1])
			#if i==2 and j==3:
			#	print(p,i)
			#print(i,j)
			if e!=j:
				ans.append((e,j))
			p=p+1
	ans=sorted(ans)
	return(ans)
import ast

def parse(inp):
  inp = ast.literal_eval(inp)
  return (inp)

fncall = input()
lparen = fncall.find("(")
rparen = fncall.rfind(")")
fname = fncall[:lparen]
farg = fncall[lparen+1:rparen]

if fname == "frequency":
  arg = parse(farg)
  print(frequency(arg))

if fname == "onehop":
  arg = parse(farg)
  print(onehop(arg))
