class Course:

    def __init__(self, c_id: int, title: str, code: str,teacher_name:str, day: str):
        self.c_id = c_id
        self.title = title
        self.code = code
        self.teacher_name = teacher_name
        self.day = day


    def save(self):
        print(f"{self.title} {self.code} has been saved.")


course1=Course(1,"python","201","sara","mon")

Course.save(course1)