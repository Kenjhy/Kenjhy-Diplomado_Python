
#region dsdd
def h():
    if True:
        print("if1")
        if True:
            print("elseif")
            return 0
        if True:
            print("if2")
    if False:
        print("sss")
    else:
        print("eee")

#endregion        
x = h()
print(x)

