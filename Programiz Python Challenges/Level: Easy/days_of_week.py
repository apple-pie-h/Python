def day_of_week(n):
    days = [
        "Error",  # index 0, for out of range
        "Monday", 
        "Tuesday", 
        "Wednesday", 
        "Thursday", 
        "Friday", 
        "Saturday", 
        "Sunday"
    ]
    
    if 1 <= n <= 7:
        return days[n]
    else:
        return "Error"
