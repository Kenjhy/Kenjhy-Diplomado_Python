
#Alcances, cuando si y cuando 
#Cuando no podemos acceder a una variable fuera 
# def scopeTest():
#     x = 123
    
# scopeTest()
# print(x)

def miFunction():
    print("No conozco la variable?", var)    
var = 1
miFunction()
var2 = 2
print(var)

def miFunction2():
    var_x = 2
    print("No conozco la variable2?", var_x)    

var_x = 3
miFunction2()
var2 = 2
print(var_x)

def miFunction3():
    global var_y
    var_y = 3
    print("Conozco a a quella variable", var_y)

var_y = 1
miFunction3()
print(var_y)

#Diferentes espacios de memoria

def miFunction4(n):
    print("Yo obtube", n)
    n+=1
    print("yo ahora tengo",n)
    
var_h = 1
miFunction4(var_h)
print(var_h)

