def isPythagoreanTriple(a,b,c):
    hypotenuse = max(a, b, c)
    if hypotenuse == a:
        return hypotenuse**2 == b**2 + c**2
    elif hypotenuse == b:
        return hypotenuse**2 == a**2 + c**2
    else:
        return hypotenuse**2 == a**2 + b**2

print(isPythagoreanTriple(3,4,5))