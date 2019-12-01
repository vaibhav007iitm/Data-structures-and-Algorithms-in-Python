import math
def expanding(l):
	a=abs(l[1]-l[0])
	for i in range(1,len(l)-1):
		b=abs(l[i+1]-l[i])
		if b<=a:
			return False
		a=b
	else:
		return True
def accordian(l):
	a=abs(l[1]-l[0])
	b=abs(l[2]-l[1])
	if a>b:
		for i in range(2,len(l)-1):
			c=abs(l[i+1]-l[i])
			if i%2==0 and b>=c:
				return False
			if i%2!=0 and b<=c:
				return False
			a=b
			b=c
		else:
			return True
	elif a<b:
		for i in range(2,len(l)-1):
			c=abs(l[i+1]-l[i])
			if i%2==0 and b<=c:
				return False
			elif i%2!=0 and b>=c:
				return False
			a=b
			b=c
		else:
			return True
	else:
		return False
def rotate(l):
	ans=[x[:] for x in l]
	n=len(l)
	for i in range(n):
		for j in range(n):
			ans[i][j]=l[n-1-j][i]
	return ans
import ast

def parse(inp):
  inp = ast.literal_eval(inp)
  return (inp)

fncall = input()
lparen = fncall.find("(")
rparen = fncall.rfind(")")
fname = fncall[:lparen]
farg = fncall[lparen+1:rparen]

if fname == "expanding":
  arg = parse(farg)
  print(expanding(arg))

if fname == "accordian":
  arg = parse(farg)
  print(accordian(arg))

if fname == "rotate":
  arg = parse(farg)
  savearg = []
  for row in arg:
    savearg.append(row[:])
  ans = rotate(arg)
  if savearg == arg:
    print(ans)
  else:
    print("Side effect")
