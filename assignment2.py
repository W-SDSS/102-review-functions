def isHappy(float):
    return float > 0 and isinstance(float, int)

print(isHappy(9))
print(isHappy(0.98))