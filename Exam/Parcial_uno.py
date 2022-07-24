# print("2")
# def fun(x):
#     if x % 2 == 0:
#         return 1
#     else:
#         return 2

# print(fun(fun(2)))

# print("3")
# def fun(inp=2, out=3):
#     return inp * out


# print(fun(out=2))

# print("7")
# x = int(input())
# y = int(input())
# x = x % y
# x = x % y
# y = y % x
# print(y)

# print("9")
# lst = [i for i in range(-1, -2)]
# print(lst)

# print("12")
# dct = {'one': 'two', 'three': 'one', 'two': 'three'}
# v = dct['three']

# for k in range(len(dct)):
#     v = dct[v]

# print(v)

# print("14")
# x = 1
# y = 2
# x, y, z = x, x, y
# z, y, z = x, y, z

# print(x, y, z)

# print("15")
# tup = (1, 2, 4, 8)
# tup = tup[-2:-1]
# tup = tup[-1]
# print(tup)

# print("16")
# dd = {"1": "0", "0": "1"}
# for x in dd.vals():
#     print(x, end="")

# print("17")
# def function_1(a):
#     return None


# def function_2(a):
#     return function_1(a) * function_1(a)


# print(function_2(2))

#19
# my_tuple=(1,2,3)
# my_tuple[1] = my_tuple[1] + my_tuple[0]

#21
# my_list =  [x * x for x in range(5)]


# def fun(lst):
#     del lst[lst[2]]
#     return lst


# print(fun(my_list))
#24
# lst = [[x for x in range(3)] for y in range(3)]

# for r in range(3):
#     for c in range(3):
#         if lst[r][c] % 2 != 0:
#       	    print("#")

#26
# i = 0
# while i < i + 2 :
#     i += 1	
#     print("*")
# else:
#     print("*")

#28
# def fun(a, b, c=0):
#     # Cuerpo de la función.

#31
# nums = [1, 2, 3]
# vals = nums
# del vals[:]

#31
# z = 0
# y = 10
# x = y < z and z > y or y > z and z < y
# print(x)

# try:
#     print(5/0)
#     break
# except:
#     print("Lo siento, algo salió mal...")
# except (ValueError, ZeroDivisionError):
#     print("Mala suerte...")

# in = 0
# In = 0
# print = 0
# for =0

# y = input()
# x = input()
# print(x + y)

try:
    value = input("Ingresa un valor: ")
    print(int(value)/len(value))
except ValueError:
    print("Entrada incorrecta...")
except ZeroDivisionError:
    print("Entrada errónea...")
except TypeError:
    print("Entrada muy errónea...")
except:
    print("¡Buuu!")

