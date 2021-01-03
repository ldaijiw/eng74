from datetime import date

def has_bday_passed(year, month, day):
    '''
    Evaluates if birthday has passed (inclusive) the current date or not
    Returns True if it has passed, otherwise False

    '''

    today = date.today()
    try:
        bday = date(year, month, day)
    except ValueError:
        print("\nInvalid date given.")
        return
    
    if bday.month < today.month:
        return True
    elif bday.month > today.month:
        return False
    elif bday.day <= today.day:
        return True
    else:
        return False
    
    