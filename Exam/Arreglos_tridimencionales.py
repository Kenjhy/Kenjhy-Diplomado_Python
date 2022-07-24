rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]
# print(rooms)
rooms[2][14][19] = True
vacancy = 0

for room_number in range(20):
    print("if", rooms[2][14][room_number])
    if rooms[2][14][room_number]:
        print("romnum",room_number)
        print("ooom", rooms)
        vacancy += 1
        
print(vacancy)