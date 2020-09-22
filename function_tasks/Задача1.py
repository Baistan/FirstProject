def distance(x1,x2,y1,y2):
    import math
    AC = x2 - x1
    BC = y2 - y1
    AB = math.sqrt(AC ** 2) + math.sqrt(BC ** 2)
    return AB
print(distance(2,4,3,4))