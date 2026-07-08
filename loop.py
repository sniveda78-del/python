    #   RANGE
# for i in range(1,10):
#  print(i)
# else:
#  print('loop completed')

#      LIST
# for i in [1,2,3,4,5,6,7]:
#   print(i)

#      SET
# for i in {1,2,3}:
#     print(i)

#       TUPLE
# for i in(1,2,3,4,5,7):
#     print(i)

#      STRING
# for i in ("hello"):
#     print(i)

#    MAPING
# for i in {1:"one",2:"two",3:"three"}:
#  print(i)

#   MULTIPLICATION TABLE OF 5
# for i in [1,2,3,4,5,6,7,8,9,10]:
#     print(f"{i}*{5}={i*5}")
 

#      FACTORIAL OF A NUMBER
# x=int(input("enter"))
# sum=1
# for i in range(1,x+1):
#     sum=sum*i
# print('factorial',sum)


#      FIBANNOCI SERIES
# x=int(input("enter"))
# a,b=0,1
# for i in range(x):
#     print(a)
#     c=a+b
#     a=b
#     b=c
    
# n=5
# for i in range (n):
#     print("*"*(i+1))

# n=int(input("enter"))
# for i in range(1,n+1):
#     print(" "*(n-i),(str(i)+" ")*i)

# n=5
# for i in range(n,0,-1):
#     print(" "*(n-i),"* "*i)


 
# print(ord('A'))
# print(chr(68))

# n=26
# for i in range(0,n+1):
#     print(chr(65+i))

# n=26
# for i in range(0,n+1):
#     print(chr)

# x=int(input("enter"))
# for i in range(0,x+1):
#     print(" "*(x-1)*i)
# for j in range(i):
#     print(chr(64+j)*j)
#     print()

# x=int(input("enter"))
# i=5
# while i<=x:
#     print(" * "*i)

# temp=int(input("enter the c: "))   
# if temp <20:
#     print("cold")
# elif temp >=20 and temp <=30:
#     print("warm")
# elif temp >31:
#     print("too hot")
# else:
#     print("plasent")    
 
# LIST TO TUPLE
# x=[1,2,3,4,5]
# y=tuple(x)
# print()

# x=[1,2,3]
# y=tuple(x)
# print(y)
# print(len(y))
# print(y[1:2:1])
# print(y[::-1])


# t=(4, )
# print(type(t))

# t=(2,4,6,8)
# p=(1,3,5,7)
# print(t+p)
# print(t in p)
# print(p*3)

# for i in (2,3,4,5,6):
#     print(i)

# a=['H','E','L','L','O']
# print(a.count('L'))    

# t=(1,2.5,[5,7.6,'hello'],10)
# t[2][2]='hai'
# print(t)
# t[2].append(3)
# print(t)
# a,b,c,d=t
# print(a)
# print(b)
# print(c)
# print(d)
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))

# r=range(1,10,2)
# print(list(r))
# print(len(r))
# print(r[2:3:1])
# print(r[6:1:-1])

# numbers=frozenset([1,2,3,4])
# print(numbers)
# x={1,2,3}
# print(x)
# x={1,2,3,3,5}
# print(type(x))
# print(len(x))
# print(x)

# x={1,5,7,8,9}
# x.add(4)
# print(x)
# x.update([2,6])
# print(x)

# TO REMOVE 
# a={1,2,3,4}
# a.remove(2)
# print(a) 

# DISCARD-TO REMOVE ELE WITHOUT ERROR
# a={1,2,3,4}
# a.discard(5)
# print(a)

# POP
# x={1,2,3}
# x.pop()
# print(x)

# CLEAR
# x={1,2,3}
# x.clear()
# print(x)

# UNION
# a={1,3,5}
# b={2,4,6}
# print(a|b)

# INTERSECTION
# a={2,3,5,6}
# b={2,1,4,7}
# print(a&b)

# DIFFERENCE
# a={1,2,3,4,5}
# b={2,3,4,5,6,7,8}
# print(a-b)

# SYMMETRIC DIFFERENCE
# a={2,7,8,9}
# b={5,9,3,5}
# print(a^b)

# ISSUBSET
# a={1,2,3,4,5,6,7}
# b=(2,4,8)
# print(a.issubset(b))

# ISSUPERSET
# a={1,3,7}
# b={3,8,9}
# print(a.issuperset(b))

# COPY
# a={1,3}
# b={5,8}
# b=a.copy()
# print(b)

# SORT
# a={1,3,2,7,8}
# print(sorted(a))

# MAX AND MIN
# a={2,6,9}
# print(max(a))
# print(min(a))

# SUM
# a={1,4,9,7}
# print(sum(a))
