def first_n_vowels(string, n):
    vowels = "AEIOUaeiou"
    found_vowels = ""
    for char in string:
        if char in vowels:
            found_vowels += char
            if len(found_vowels) >= n:
                vow=list( "".join(found_vowels))
                return vow # Return the first n vowels

    return "Not found"
      
