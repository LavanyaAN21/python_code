#FUNCTIONS
def even(a):
    if a%2==0:
        print("even")
    else:
         print(" not even")
even(2)


def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
print(fact(4))

def sum(a,b):
    return(a+b)
c=sum(5,4)
print(c)

#packing
def package(*a):
    print(a)
package(1,2,3,4)

def pack(**a):
    print(a)
pack(i=2)

def display_1(a,b,c):
    print(a,b,c)
display_1(*(1,2,3))

def dis(a,b,c):
    print(a,b,c)
dis(*{'h':1,'e':2,'l':3})

#variable agr   \\*- agrument, **-keywordagr
def c(*a,**b):
    print(a)
    print(b)
c(1,2,3,h=1,a=2)
