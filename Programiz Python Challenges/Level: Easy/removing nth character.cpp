def remove_ith_character(string, i):
    if i< 0 or i >= len(string):
        return "Index out of range"
    return string[:i] + string[i+1:]
