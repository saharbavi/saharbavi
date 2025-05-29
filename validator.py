import re


def course_validator(course):
    errors = []
    if not (type(course[0]) == int and course[0] > 0):
        errors.append('Course ID must be an integer > 0')

    if not (type(course[1]) == str and re.match(r"^[a-zA-Z\s]{3,30}$", course[1])):
        errors.append('Course Name is Invalid')

    if not (type(course[2]) == str and re.match(r"^\d{3}$", course[2])):
        errors.append('Course Code is Invalid')

    if not (type(course[3]) == str and re.match(r"^[a-zA-Z\s]{3,30}$", course[3])):
        errors.append('Course day is Invalid')

    if not (type(course[4]) == str and re.match(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", course[4])):
        errors.append('Course date is Invalid')

    if not (type(course[5]) == str and re.match(r"^[a-zA-Z\s]{3,30}$", course[5])):
        errors.append('Teacher name is Invalid')

    return errors
