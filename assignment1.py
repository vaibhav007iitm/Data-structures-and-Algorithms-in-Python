import math
def isprime(n):
	if n==1 or n<=0:
		return(False)
	j=int(math.sqrt(n))
	for i in range(2,j+1):
		if n%i==0:
			return(False)
	return(True)
def intreverse(n):
	n=str(n)
	ans=n[-1]
	for i in range(len(n)-2,-1,-1):
		ans=ans+n[i]
	n=int(ans)
	return(n)
def matched(s):
	count=0
	for i in range(0,len(s)):
		if s[i]=='(':
			count+=1
		elif s[i]==')':
			count-=1
		if count<0:
			return(False)
	if count==0:
		return(True)
	else:
		return(False)

def sumprimes(l):
	ans=0;
	for i in l:
		if isprime(i):
			ans+=i
	return (ans)


import ast

def tolist(inp):
  inp = "["+inp+"]"
  inp = ast.literal_eval(inp)
  return (inp[0],inp[1])

def parse(inp):
  inp = ast.literal_eval(inp)
  return (inp)

fncall = input()
lparen = fncall.find("(")
rparen = fncall.rfind(")")
fname = fncall[:lparen]
farg = fncall[lparen+1:rparen]

if fname == "intreverse":
   arg = parse(farg)
   print(intreverse(arg))
elif fname == "matched":
   arg = parse(farg)
   print(matched(arg))
elif fname == "sumprimes":
   arg = parse(farg)
   print(sumprimes(arg))
else:
   print("Function", fname, "unknown")
