def is_cubic_square(n):
    a=int(n**(1/2))
    b=round (n**(1/3))
    if (a*a==n and b*b*b==n):
        return True
    return False
