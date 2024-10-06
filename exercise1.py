num = int(input("Put the whole number: "))
exponent = int(input("Put the exponent: "))

def power(num, exponent):
    if exponent == 1:
        return 1
    else:
        return num * power(num, exponent-1)

power(num, exponent)