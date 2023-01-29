import math
def deg_to_rad(d: int) -> float:
    x = 180 / d
    res = math.pi / x
    return res
def calc_sin(ang: float) -> float:
    n = 1
    t1 = ang**n/math.factorial(n)
    
    n = n+2
    t2 = ang**n/math.factorial(n)
    sum = 0 
    while n<110:
        sum = (sum + t1) - t2
        n = n+2
        t1 = ang**n/math.factorial(n)
        n = n+2 
        t2 = ang**n/math.factorial(n)
    sum = sum + t2
    sum = round(sum, 5)
    return sum
o = str(input("Please enter a trigonometric function (for a list of supported functions ennter ""help""): "))
funcs = ["sin", "cos", "tg", "ctg"]
a = -1

while (True):
    o = str(input("Please enter a trigonometric function (for a list of supported functions ennter ""help""): "))
    a = -1
    if o.strip() == "help":
        print(funcs)
        
    else:
        for i in range(len(funcs)):
            if o.strip() == funcs[i]:
                a = i
    if a != -1: 
        b = int(input("Please enter an angle (deg): "))
        fun = [calc_sin(deg_to_rad(b)), calc_sin(round(math.pi/2, 5) - deg_to_rad(b)), 
        calc_sin(deg_to_rad(b))/calc_sin(round(math.pi/2, 5)- deg_to_rad(b)), 1/(calc_sin(deg_to_rad(b))/calc_sin(round(math.pi/2, 5)- deg_to_rad(b)))]
        print(fun[a])
    a = -1

