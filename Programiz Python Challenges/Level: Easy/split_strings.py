def split_string(s):
    vowels = "AEIOUaeiou"
    vowel_string = ""
    consonant_string = ""

    for char in s:
        if char in vowels:
            vowel_string += char
        elif char.isalpha():  # Check if it's a consonant (a letter)
            consonant_string += char

    return vowel_string, consonant_string
