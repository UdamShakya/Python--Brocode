
def is_weekend(day):
    match day:
        case 'saturday' | 'sunday':
            return True
        case _:
            return False

def day_of_week(day):
    match day:
        case 'monday':
            return "Start of the work week"
        case 'tuesday':
            return "Second day of the work week"
        case 'wednesday':
            return "Midweek"
        case 'thursday':
            return "Almost there"
        case 'friday':
            return "Last work day"
        case 'saturday' | 'sunday':
            return "Weekend"
        case _:
            return "Invalid day"
        

print(day_of_week('monday'))
