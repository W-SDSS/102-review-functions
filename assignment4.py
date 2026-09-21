def isPythagoreanTriple(a,b,c):
    if hypotenuse**2 == min**2 + middle**2:
        return True
    else:
        return False



a = float(input("Enter a number1: "))
b = float(input("Enter a number2: "))
c = float(input("Enter a number3: "))

numbers = [a, b, c]
hypotenuse = max(numbers)
min = min(numbers)
middle = 
