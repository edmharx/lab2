length = int(input("Input the length of the sides: "))

for i in range(length):
    if i == length-1 or i == 0:
        print("x"*length)
    else:
        print("x"+" "*(length-2)+"x")