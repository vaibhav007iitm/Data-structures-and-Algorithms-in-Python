#question1

myinput = '''
[-1,-2,-3]
'''

def maxbad(l):
  mymax = 0
  for i in range(len(l)):
    if l[i] > mymax:
       mymax = l[i]
  return(mymax)

import ast

try:
   myarg =  ast.literal_eval(myinput.strip())
except:
   print(False)
else:
  try:
     print(maxbad(myarg) != max(myarg))
  except:
     print(False)

#question2

myinput = '''
[(1,2),(3,2)]
'''

def stablesortbad(l):
  for j in range(len(l)-1):
    for i in range(len(l)-1):
      if l[i][1] >= l[i+1][1]:
        (l[i],l[i+1]) =  (l[i+1],l[i])
  return(l)    
    
def stablesortgood(l):
  for j in range(len(l)-1):
    for i in range(len(l)-1):
      if l[i][1] > l[i+1][1]:
        (l[i],l[i+1]) =  (l[i+1],l[i])
  return(l)    
    
import ast

try:
   myarg =  ast.literal_eval(myinput.strip())
except:
   print(False)
else:
  try:
     print(stablesortbad(myarg[:]) != stablesortgood(myarg[:]))
  except:
     print(False)

#question3

def thirdmin(l):
  (mymin,mysecondmin,mythirdmin) = (1000000,1000000,1000000)
  for i in range(len(l)):
    # Your code below this line
    l.sort()
    (mymin,mysecondmin,mythirdmin)=(l[0],l[1],l[2])
    # Your code above this line
  return(mythirdmin)

import ast

def tolist(inp):
  inp = ast.literal_eval(inp)
  return(inp)

fncall = input()
lparen = fncall.find("(")
rparen = fncall.rfind(")")
fname = fncall[:lparen]
farg = fncall[lparen+1:rparen]

if fname == "thirdmin":
  arg = tolist(farg)
  print(thirdmin(arg))

#question4

def oddpositions(l):
  if len(l) <= 1:
    return([])
  else:
    return(
       # Complete the recursive call below this line
l[1:2]+oddpositions(l[2:])
       # Complete the recursive call above this line
    )

import ast

def tolist(inp):
  inp = ast.literal_eval(inp)
  return(inp)

fncall = input()
lparen = fncall.find("(")
rparen = fncall.rfind(")")
fname = fncall[:lparen]
farg = fncall[lparen+1:rparen]

if fname == "oddpositions":
  arg = tolist(farg)
  print(oddpositions(arg))

#question5

from math import *
def sumof3squares(n):
  #if n==3:
  #	return True
  #if n==1 or n==2:
   # return False
  for i in range(1,int(sqrt(n-2)+1)):
    for j in range(1,int(sqrt(n-2)+1)):
      for k in range(1,int(sqrt(n-2))+1):
        if ((i*i)+(j*j)+(k*k))==n:
          return True
  else:
    return False
import ast

def toint(inp):
  inp = ast.literal_eval(inp)
  return (inp)

fncall = input()
lparen = fncall.find("(")
rparen = fncall.rfind(")")
fname = fncall[:lparen]
farg = fncall[lparen+1:rparen]

if fname == "sumof3squares":
  arg = toint(farg)
  print(sumof3squares(arg))

#question6

def intersect(l1,l2):
  s1=set(l1)
  s2=set(l2)
  s3=s1 & s2
  l=list(s3)
  l.sort()
  return (l)
import ast

def topairoflists(inp):
    inp = "["+inp+"]"
    inp = ast.literal_eval(inp)
    return (inp[0],inp[1])

fncall = input()
lparen = fncall.find("(")
rparen = fncall.rfind(")")
fname = fncall[:lparen]
farg = fncall[lparen+1:rparen]

if fname == "intersect":
   (arg1,arg2) = topairoflists(farg)
   print(intersect(arg1,arg2))

#question7

p=input()
ans=''
i=input()
while(i):
  if(i.find(p)!=-1):
    ans=i
  i=input()
print(ans)

#question8

from statistics import mean
def maxaverage(l):
  score={}
  for i in range(len(l)):
    try:
      score[l[i][0]]=score[l[i][0]]+[l[i][1]]
    except:
      score[l[i][0]]=[l[i][1]]
  k=list(score.keys())
  for i in k:
    score[i]=mean(score[i])
  v=sorted(score.values(),reverse=True)
  high=v[0]
  ans=[]
  for i in k:
    if score[i]==high:
      ans.append(i)
  ans.sort()
  return ans
    
import ast

def tolist(inp):
  inp = ast.literal_eval(inp)
  return (inp)

fncall = input()
lparen = fncall.find("(")
rparen = fncall.rfind(")")
fname = fncall[:lparen]
farg = fncall[lparen+1:rparen]

if fname == "maxaverage":
  arg = tolist(farg)
  print(maxaverage(arg))
