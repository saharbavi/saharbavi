class Teacher:

    def __init__(self,t_id:int,name:str,family:str,birth_date:str):
        self.t_id = t_id
        self.name = name
        self.family = family
        self.birth_date = birth_date


    def save(name, family):
        print("Teacher:",name+" "+family+" saved!")

#
# teach1=Teacher(12,"sara","alipour","1998")
#
# Teacher.save(teach1.name,teach1.family)