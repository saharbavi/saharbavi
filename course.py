from  validator import *

class Course:

    def __init__(self, course_id: int, course_name: str, course_code: str, course_day: str, course_date: str,
                 teacher_name: str):
        self.course_id = course_id
        self.course_name = course_name
        self.course_code = course_code
        self.course_day = course_day
        self.course_date = course_date
        self.teacher_name = teacher_name

    def save(self):

        print(f"{self.course_id} {self.course_name} {self.course_code} {self.course_day} {self.course_date} {self.teacher_name}  has been saved.")


course1 = Course(1, "python", "201", "mon", "1404-07-12" , "sara")
print(course_validator(course1))
Course.save(course1)
