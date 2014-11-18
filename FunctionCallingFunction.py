def cube(number):
    #This is a test comment on this function
    return number**3

def by_three(number):
    if number % 3 == 0:
        return cube(number)
    else:
        return False