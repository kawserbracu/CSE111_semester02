# -*- coding: utf-8 -*-
"""CSE111,Ass-01,summer'23.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sCcg3DR8g0X-wnU8qDvafWz1pfUSxhcs

Task1
"""

st=input()
up=0
nst=""
for i in st:
  if 65<=ord(i)<=90:
    up+=1
lc=len(st)-up
if lc>=up:
  for i in st:
    if 65<=ord(i)<=90:
      nst+=chr(32+ord(i))
    elif 97<=ord(i)<=122:
      nst+=i
else:
  for i in st:
    if 65<=ord(i)<=90:
      nst+=i
    elif 97<=ord(i)<=122:
      nst+=chr(ord(i)-32)
print(nst)

"""Task2"""

ui=input()
count=0
for i in ui:
  if 48<=ord(i)<=57:
    count+=1
if len(ui)==count:
  print("NUMBER")
elif 0<count<len(ui):
  print("MIXED")
else:
  print("WORD")

"""Task3"""

ui=input()
ou=""
count=0
for i in ui:
  if 65<=ord(i)<=90:
    count+=1
  elif count==1:
    ou+=i
  elif count==2:
    break
if ou=='':
  print("BLANK")
else:
  print(ou)

n=input()
for i in range(len(n)):
   if 65<=ord(n[i])<=90:
      start=i
      break

for j in range(len(n)):
   if 65<=ord(n[j])<=90:
      end=j

if len(n[start+1:end:1])==0:
  print("BLANK")
else:
  print(n[start+1:end:1])

"""Task4"""

ui1,ui2=input(),input()
ou=""
for i in ui1:
  for j in ui2:
    if ord(i)==ord(j):
      ou+=i
      break
for i in ui2:
  for j in ui1:
    if ord(i)==ord(j):
      ou+=i
      break
print(ou)

"""Task5"""



"""L-1"""

list1=[]
list2=[]
ip=0
while True:
    ip=input()
    if ip!="STOP":
      list1.append(int(ip))
    else:
      break
for i in range(len(list1)):
  for j in range(len(list1)):
    if list1[i]==list1[j]:
      count+=1
  if list1[i] not in list2:
    print(f"{list1[i]} - {count} times")
  list2.append(list1[i])
  count=0

"""L2"""

ip=int(input())
list1=[]
sum1=0

for i in range(ip):
  sum=0
  inp=input().split()
  for j in range(len(inp)):
    sum+=int(inp[j])

  if sum>sum1:
    sum1=0
    if len(list1)>0:
      for d in range(len(inp)):
        list1[d]=int(inp[d])
    else:
      for d in range(len(inp)):
        list1.append(int(inp[d]))
    for x in range(len(list1)):
      sum1+=list1[x]
print(sum1)
print(list1)

"""L-3"""

list1=input().split()
for i in range(len(list1)):
  list1[i]=int(list1[i])
list2=input().split()
for i in range(len(list2)):
  list2[i]=int(list2[i])
list3=[]
for i in range(len(list1)):
  for j in range(len(list2)):
    list3.append(list1[i]*list2[j])
print(list3)

"""L4"""

while True:
  list1=[]
  flag="UB Jumper"
  ui=input()
  if ui=="STOP":
    break
  else:
    ui=ui.split()
    for i in range(len(ui)-1):
      list1.append(i+1)
    for j in range(len(ui)-1):
      sb=abs(int(ui[j+1])-int(ui[j]))
      if sb not in list1:
        flag="Not UB Jumper"
        break
      else:
        flag="UB Jumper"
    print(flag)

"""L5

"""

nk=input().split()
n,k=int(nk[0]),int(nk[1])
y=input().split()
count=0
if len(y)==n :
  for i in range(n):
    if 0<=int(y[i])<=5 and 5-int(y[i])>=k:
      count+=1
  print(count//3)

"""DT1"""

ui=input().split(",")

