from course import Course
from teacher import Teacher



course1=Course(1,"python","201","sara","mon")
teach1=Teacher(12,"sara","alipour","1998")

Teacher.save(teach1)
Course.save(course1)