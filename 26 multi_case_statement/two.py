def is_weekend(day):
    match day:
        case "saturday" | "sunday":                     #|-->logical operator OR
            return True
        case "monday" |"tuesday"|"wednesday"|"thursday"|"friday":
            return False
        case _:
            return False

print(is_weekend("saturday"))        #true  
print(is_weekend("friday"))          #false
print(is_weekend("pizza"))           #false