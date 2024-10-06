height = int(input("Enter the height of the triangle: "))

for i in range(height):
    new_height = height-1
    print("*"*(new_height+1))
    height = new_height