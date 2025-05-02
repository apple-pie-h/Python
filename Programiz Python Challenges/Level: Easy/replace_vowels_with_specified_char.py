def replace_vowels(string, char):
    for vowel in "AEIOUaeiou":
        string=string.replace(vowel,char)
    return string
