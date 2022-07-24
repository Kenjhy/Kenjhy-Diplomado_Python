i = 2
while i >=0:
    print("*")
    i -=2
    
for i in range(-1,1):
    print("#")
    
z = 10
y=0
x=z>y or z==y
print(x)

m=[3,1,-1]
m[-1]=m[-2]
print(m)


for i in range(1):
    print("#")
else:
    print("#")
    
t = [[3-i for i in range(3)] for j in range(3)]
s = 0
for i in range(3):
    s+=t[i][i]
print(s)
    
    
m=[3,1,-2]
print(m[m[-1]])

i = 0
while i <= 5:
    i+= 1
    if i % 2 ==0:
        break
print("*")


print("Q5")
var = 0
while var < 6:
    var += 1
    if var % 2 ==0:
        continue
    print("*")

print("Q6")
a=1
b=0
c=a&b
d=a|b
e=a^b

print(c+d+e)

print("Q7")
mm=[i for i in range(-1,2)]
print(mm)

print("Q8")
nums=[1,2,3]
vals = nums[-1:2]
print(vals)

print("Q9")
var = 1
while var < 10:
    print("#")
    var = var << 1
    
print("Q10")
vals=[0,1,2]
vals[0], vals[2] = vals[2], vals[0]
print(vals)

print("Q12")
i = 0
while i <= 3:
    i += 2
    print("*")

print("Q15")
my_list_1 = [1,2,3]
my_list_2 = []
for v in my_list_1:
    my_list_2.insert(0,v)
print(my_list_2)