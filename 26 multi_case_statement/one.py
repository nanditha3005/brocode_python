#match-case-statement= is an alternative to using many 'elif' statements
#                      execute some code if a value matches a 'case'
#                      benefits--cleaner and syntax is more readable

def day_of_Week(day):
    if day==1:
        return "Its Sunday"
    elif day==2:
        return "Its Monday"
    elif day==3:
        return "Its Tuesday"
    elif day==4:
        return "Its Wednesday"
    elif day==5:
        return "Its Thursday"
    elif day==6:
        return "Its Friday"
    elif day==7:
        return "Its Saturday"
    else:
        return "Not a valid day"
    

print(day_of_Week(1))       #Its Sunday
print(day_of_Week(9))       #Not a valid day


#using match-case_statemet
def day_of_weeks(day):
    match day:
        case 1:
            return "Its Sunday"
        case 2:
            return "Its Monday"
        case 3:
            return "Its Tuesday"
        case 4:
            return "Its Wednesday"
        case 5:
            return "Its Thursday"
        case 6:
            return "Its Friday"
        case 7:
            return "Its Saturday"
        case _:
            return "Not a valid day"
        
print(day_of_weeks(3))                  #Its Tuesday
print(day_of_weeks(8))                  #Not a valid day