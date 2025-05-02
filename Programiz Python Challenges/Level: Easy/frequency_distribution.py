from collections import Counter

def frequency_distribution(lst):
    frequency_count=Counter(lst)
    dictionary=dict(frequency_count)
    return dictionary
