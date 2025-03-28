##Sorting based on Mass or bulky item

def sort(width, height, length, mass):
    volume = width * height * length
    if volume >= 1000000 or width >= 150 or height >= 150 or length >= 150:
        if mass >= 20:
            return "REJECTED"
        else:
            return "SPECIAL"
    elif mass >= 20:
        return "SPECIAL"
    else:
        return "STANDARD"
