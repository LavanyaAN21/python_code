a = "1EW22CS4@#"
num_count = 0
alpa_count = 0
spl_count = 0
i = 0
while i < len(a):
    if '0' <= a[i] <= '9':
        num_count += 1
    elif 'a' <= a[i] <= 'z' or 'A' <= a[i] <= 'Z':
        alpa_count += 1
    else:
        spl_count += 1
    i += 1
print("Count of numbers:", num_count)
print("Count of alphabets:", alpa_count)
print("Count of special characters:", spl_count)

#WAPT extract only spl char
a = "1EW22CS4@#"
spl = ""
i = 0
while i < len(a):
    if not ('0' <= a[i] <= '9' or 'a' <= a[i] <= 'z' or 'A' <= a[i] <= 'Z'):
        spl=spl+a[i]
    i += 1
print("Special characters:", spl)

c=['hi','90','hello',90]
c.pop(int)
print(c)


e='okay!bye'
count=0
i=0
while i<len(e):
    if e[i] in ('a','e','i','o','u'):
        count=count+1
    i=i+1
print(count)


p=['hi','Python']
i=0
a=[]
while i<len(p):
    a=a+[len(p[i])]
    i+=1
print(a)

b=['Hi','Python']
i=0
c=[]
while i<len(b):
    if b[i]=='':
        c=c+'_'
    else:
        c=c+[b[i]]
    i+=1
print(c)

#1
d = "Hi"
e=["Python", "SQL"]
b = {}
i=0
while i < len (d):
    b[d[1]] = e[i]
    i=i+1
print (b)'''

#2
E= ['python', 'sql']
k = {}
i=0
while i<len (E):
    k[E[i]] = len (E[i])
    i=i+1
print(k)

#3
a='aabbccc'
b=''
i=0
while i<len(a):
    if a[i] not in b:
       b=b+a[i] + str(a.count(a[i]))
    i=+1
print(b)


#5
n=4
i=1
fact=1
while i<=n:
    fact=fact*i
    i=i+1
print(fact)

#6

num = int(input("Enter a number: "))
sum = 0
i = 1
while i < num:
    if num%i== 0:
        sum += i
        i += 1
if sum == num:
    print("Perfect number")
else:
    print("Not a perfect number")


#for

d=['python','sql']
e=[]
for i in d:
    c=0
    for j in i:
        c=c+1
    e=e+[c]
print(e)

d=['Hello','Hi']
e=[]
for i in d:
    c=0
    for j in i:
        if j in ('aeiouAEIOU'):
            c=c+1
    e=e+[c]
print(e)

d=['Python','Workshop']
e=[]
for i in d:
    c=0
    for j in range(len(i)):
        if j%2==0:

            c=c+1
    e=e+[c]
print(e)


a='aabbcc'
b=" "
for i in a:
    if i not in b:
        c=0
        for j in a:
            if i==j:
                c = c + 1
        b=b+i+str(c)
print(b)

#not correct
a='abacbc'
b=" "
c=" "
for i in a:
    if i not in b:
        c=0
        for j in a:
            if i==j:
                c = c + 1
        b=(b+i)
c=str(c)
print(b)
