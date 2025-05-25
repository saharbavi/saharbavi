from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg
from course_manager import *
from validator import *

course_list = read_from_file("course.dat")


def load_data(course_list):
    course_list = read_from_file("course.dat")
    for row in table.get_children():
        table.delete(row)

    for course in course_list:
        table.insert("", END, values=course)


def reset_form():
    course_id.set(len(course_list) + 1)
    course_name.set("")
    course_code.set("")
    course_day.set("")
    course_date.set("")
    teacher_name.set("")
    load_data(course_list)


#
def save_btn_click():
    course = (
        course_id.get(), course_name.get(), course_code.get(), course_day.get(), course_date.get(), teacher_name.get())
    errors = course_validator(course)
    if errors:
        msg.showerror("Errors", "\n".join(errors))
    else:
        msg.showinfo("Saved", "course saved")
        course_list.append(course)
        write_to_file("course.dat", course_list)
        reset_form()


def table_select(x):
    selected_course = table.item(table.focus())["values"]
    if selected_course:
        course_id.set(selected_course[0])
        course_name.set(selected_course[1])
        course_code.set(selected_course[2])
        course_day.set(selected_course[3])
        course_date.set(selected_course[4])
        teacher_name.set(selected_course[5])


def edit_btn_click():
    pass


def remove_btn_click():
    pass


window = Tk()
window.title("Course Info")
window.geometry("820x320")

# course id
Label(window, text="Course Id:").place(x=20, y=20)
course_id = IntVar(value=1)
Entry(window, textvariable=course_id, state="readonly", width=23).place(x=80, y=20)

# Course Name
Label(window, text="Course Name:").place(x=20, y=60)
course_name = StringVar()
Entry(window, textvariable=course_name).place(x=100, y=60)

# course code
Label(window, text="Course Code:").place(x=20, y=90)
course_code = StringVar()
Entry(window, textvariable=course_code).place(x=100, y=90)

# Course Day
Label(window, text="Course Day:").place(x=20, y=120)
course_day = StringVar()
Entry(window, textvariable=course_day).place(x=100, y=120)

# Course Date
Label(window, text="Course Date:").place(x=20, y=150)
course_date = StringVar()
Entry(window, textvariable=course_date).place(x=100, y=150)

# Teacher
Label(window, text="Teacher Name:").place(x=20, y=185)
teacher_name = StringVar()
Entry(window, textvariable=teacher_name, width=19).place(x=103, y=185)

table = ttk.Treeview(window, columns=[1, 2, 3, 4, 5, 6], show="headings")
table.heading(1, text="Course Id")
table.heading(2, text="Course Name")
table.heading(3, text="Course Code")
table.heading(4, text="Course Day")
table.heading(5, text="Course Date ")
table.heading(6, text="Teacher Name")

table.column(1, width=60)
table.column(2, width=100)
table.column(3, width=100)
table.column(4, width=100)
table.column(5, width=100)
table.column(6, width=100)

table.bind("<<TreeviewSelect>>", table_select)

table.place(x=245, y=20)

# Button(window, text="Save", width=6).place(x=20, y=280)
# Button(window, text="Edit", width=6).place(x=90, y=280)
# Button(window, text="Remove", width=6).place(x=160, y=280)
# Button(window, text="Clear", width=6).place(x=230, y=280)

Button(window, text="Save", width=6, command=save_btn_click).place(x=20, y=280)
Button(window, text="Edit", width=6, command=edit_btn_click).place(x=90, y=280)
Button(window, text="Remove", width=6, command=remove_btn_click).place(x=160, y=280)
Button(window, text="Clear", width=26, command=reset_form).place(x=25, y=220)

#
reset_form()

window.mainloop()
