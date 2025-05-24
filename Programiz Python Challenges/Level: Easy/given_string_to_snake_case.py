def to_snake_case(s):
    lower=s.lower()
    a=""
    for i in lower:
        if i==" ":
            a+="_"
        else:
            a+=i

    return a
