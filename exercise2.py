size = int(input("Input the size of the array: "))
array = list(map(int, input("Enter the elements separated by space: ").split()))

for i in array:
    ans = i**3
    print(ans)