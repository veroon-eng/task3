#------------------Q1------------------------
"""numbers--> we use it to solve an equation or calculative operation
strings-->to write something
lists-->to make a list of anything like numbers,strings,both ....
tuples-->
dictionaries-->we use it to enter something and it's value like fruit and price, word and meanig,...."""
#...........................................
#------------------nuumbers------------------------
import math
x=20*5/2+(5**3)-74.75
print(x)


#1-->44
z=4*(6+5)
print(z)
#2-->29
c=4*6+5
print(c)
#3-->34
v=4+6*5
print(v)

b=3+1.5+4
print(type(b))

#root--> math.sqrt()// pow()
n=math.sqrt(25)
m=pow(5,2)
print(n)
print(m)
#...........................................
#------------------strings------------------------
a="hello"
print(a[1])
print(a[::-1])
print(a[4])
#...........................................
#------------------lists------------------------
#"Build this list [0,0,0] two separate ways."
#lis=[0:0:0]
#print(lis)

"""list3 = [1,2,[3,4,'hello']]
print(list3)
list3.remove('hello')
print(list3)"""

list4 = [5,3,4,6,1]
list4.sort()
print(list4)
#...........................................
#------------------dictionaries------------------------
d = {'simple_key':'hello'}
print(d["simple_key"])
d = {'k1':{'k2':'hello'}}
print(d["k1"]["k2"])
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d["k1"])
#print(d["k1"],d["nest_key"])
#...........................................
#------------------tuples------------------------
#tuples can not be changed
#by ordinary bracket()
#...........................................
#------------------sets------------------------
#sets have uniqe elements
list5 = [1,2,2,33,4,4,11,22,3,3,2]
set(list5)
print(list5)
#...........................................
#------------------booleans------------------------
x1=2>3
x2=3<=2
x3=3==2.0
x4=3.0==3
x5=4**.5!=2
print(x1)
print(x2)
print(x3)
print(x4)
print(x5)
# final
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]
l_one[2][0] >= l_two[2]['k1']












