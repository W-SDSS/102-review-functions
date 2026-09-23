import math

def isPerfectSquare(float):
    root = (math.sqrt(float))
    return root == int(root)

print(isPerfectSquare(100))
print(isPerfectSquare(5))
