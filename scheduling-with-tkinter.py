from random import*
from time import *
from tkinter import *
from tkinter import messagebox
from tkinter import font

def print_timetable(timetable):
    courses = {}
    z = '\n' * 50
    print(z)
    print("{:^200}".format("UIT TIME TABLE SCHEDULER"))
    sleep(1)
    print("Time Table:-")
    day = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
    slots = ['8-9', '9-10', '10-11', '11-12', '12-1', '1-2', '2-3', '3-4', '4-5']

    for row in range(len(timetable) + 1):
        print("\n")
        for col in range(len(timetable[row - 1]) + 1):
            if row == 0 and col == 0:
                print("                         ", end="")
            elif row == 0:
                print('{:^25}'.format(slots[col - 1]), end="")
            elif (row == 1 and col == 0) or (row == 2 and col == 0) or (row == 3 and col == 0) or (
                    row == 4 and col == 0) or (row == 5 and col == 0):
                print("{:^25}".format(day[row - 1]), end="")
            else:
                print("{:^25}".format(timetable[row - 1][col - 1]), end="")


def make_teacher_course_pair(teachers,courses):
    t_c_pair =[]
    courses_list = list(courses.keys())

    for course in range(len(courses_list)):
        course_x = courses_list[course]
        teacher_for_this_course = {}
        for key,val in teachers.items():
            if course_x in val:
                teacher_for_this_course[key] = val

        remove = []
        good_teacher = 0
        for key,val in teacher_for_this_course.items():
            if val[0] == course_x:
                good_teacher+=1
                continue
            else:
                remove.append(key)

        if good_teacher == 0:
            remove.clear()
            good_teacher_2 = 0
            for key,val in teacher_for_this_course.items():
                if len(val) == 2:
                    if val[1] == course_x:
                        good_teacher_2+=1
                        continue
                    else:
                        remove.append(key)
                elif len(val) == 3:
                    if val[1] == course_x:
                        good_teacher_2 += 1
                        continue
                    elif val[2] == course_x:
                        good_teacher_3 +=1
                        continue
                    else:
                        remove.append(key)

            for key in remove:
                del teacher_for_this_course[key]


        else:
            for key in remove:
                del teacher_for_this_course[key]

        if len(teacher_for_this_course.items()) > 1 :

            best_match = {}
            for key,val in teacher_for_this_course.items():
                if len(val) == 1 and val[0]==course_x:
                    best_match[key] = val
            if len(best_match) == 0:
                choice_teacher = choice(list(teacher_for_this_course))
                t_c_pair.append(str(choice_teacher)+'/'+str(courses_list[course]))
            elif len(best_match) == 1:
                for key,val in best_match.items():
                    t_c_pair.append(key+'/'+courses_list[course])
            elif len(best_match) > 1:
                choice_teacher = choice(list(best_match))
                t_c_pair.append(str(choice_teacher)+'/'+str(courses_list[course]))

        else:

            for key,val in teacher_for_this_course.items():
                t_c_pair.append(str(key)+'/'+str(courses_list[course]))

    return t_c_pair


def assign_slots(t_c_pair,courses,availability):
    timetable = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    check_pair = []
    t_c_p  = []
    for pair in t_c_pair:
        splitted = pair.split('/')
        course_in_split = splitted[1]
        teacher_in_split= splitted[0]
        count_1 = int(courses[course_in_split])
        while count_1 != 0:
            t_c_p.append(pair)
            count_1 -= 1

    count = 0
    length = len(t_c_p)

    while count<length:
        t_c = choice(t_c_p)
        splitted_for_teacher = t_c.split('/')
        splitted_for_teacher = splitted_for_teacher[0]



        r1 = randint(0, 4)
        r2 = randint(0, 8)

        if splitted_for_teacher in availability.keys():
            while r1 == availability[splitted_for_teacher]:
                r1 = randint(0, 4)

        splitted_slash = t_c.split('/')
        splitted_hyphen= splitted_slash[1].split('-')
        if 'lab' in splitted_hyphen:
            if timetable[r1][r2] == 0:
                if r2 == 8:
                    if timetable[r1][r2-1] == 0 and timetable[r1][r2-2] == 0:
                        timetable[r1][r2]     = t_c
                        count += 1
                        t_c_p.remove(t_c)
                        timetable[r1][r2 - 1] = t_c
                        count += 1
                        t_c_p.remove(t_c)
                        timetable[r1][r2 - 2] = t_c
                        count += 1
                        t_c_p.remove(t_c)
                    else:
                        continue
                elif r2 == 0:
                    if timetable[r1][r2+1] == 0 and timetable[r1][r2+2] == 0:
                        timetable[r1][r2]     = t_c
                        count += 1
                        t_c_p.remove(t_c)
                        timetable[r1][r2 + 1] = t_c
                        count += 1
                        t_c_p.remove(t_c)
                        timetable[r1][r2 + 2] = t_c
                        count += 1
                        t_c_p.remove(t_c)
                    else:
                        continue
                else:
                    if timetable[r1][r2-1] == 0 and timetable[r1][r2+1] == 0:
                        timetable[r1][r2] = t_c
                        count += 1
                        t_c_p.remove(t_c)
                        timetable[r1][r2 + 1] = t_c
                        count += 1
                        t_c_p.remove(t_c)
                        timetable[r1][r2 - 1] = t_c
                        count += 1
                        t_c_p.remove(t_c)

                    else:
                        continue



        if timetable[r1][r2] == 0:
            if t_c not in timetable[r1]:
                timetable[r1][r2] = t_c
                count += 1
                t_c_p.remove(t_c)
                continue
            elif t_c in timetable[r1]:
                counter = timetable[r1].count(t_c)
                if counter>1:
                    continue
                else:
                    index = timetable[r1].index(t_c)
                    if index == 8:
                        if timetable[r1][index-1] == 0:
                            timetable[r1][index - 1] = t_c
                            count+=1
                            t_c_p.remove(t_c)
                        else:
                            continue
                    elif index == 0:
                        if timetable[r1][index+1] == 0:
                            timetable[r1][index + 1] = t_c
                            count+=1
                            t_c_p.remove(t_c)
                        else:
                            continue
                    else:
                        if timetable[r1][index-1] == 0:
                            timetable[r1][index - 1] = t_c
                            count += 1
                            t_c_p.remove(t_c)
                        elif timetable[r1][index+1] == 0:
                            timetable[r1][index + 1] = t_c
                            count+=1
                            t_c_p.remove(t_c)
                        else:
                            continue
            else:
                continue
        else:
            continue


    return timetable


def assign_classes(timetable):
    class101 = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    class102 = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    class103 = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    class104 = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    class105 = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    lab101 = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    lab102 = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    lab103 = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    for eachday in range(len(timetable)):
        for eachslot in range(len(timetable[eachday])):
            if timetable[eachday][eachslot]!=0:
                splitted_slot = timetable[eachday][eachslot].split('/')
                if len(splitted_slot)>2:
                    continue
                else:
                    splitted_for_lab = splitted_slot[1].split('-')
                    if 'lab' in splitted_for_lab:
                        freelab = []
                        if lab101[eachday][eachslot] == 0:
                            freelab.append('lab101')
                        if lab102[eachday][eachslot] == 0:
                            freelab.append('lab102')
                        if lab103[eachday][eachslot] == 0:
                            freelab.append('lab103')
                        choice_lab = choice(freelab)
                        if eachslot == 0:
                            if (timetable[eachday][eachslot+1] == timetable[eachday][eachslot]) and (timetable[eachday][eachslot+2] == timetable[eachday][eachslot]):
                                timetable[eachday][eachslot] = timetable[eachday][eachslot] + '/' + choice_lab
                                timetable[eachday][eachslot+1] = timetable[eachday][eachslot+1] + '/' + choice_lab
                                timetable[eachday][eachslot+2] = timetable[eachday][eachslot+2] + '/' + choice_lab
                        elif eachslot == 8:
                            if (timetable[eachday][eachslot-1] == timetable[eachday][eachslot]) and (timetable[eachday][eachslot-2] == timetable[eachday][eachslot]):
                                timetable[eachday][eachslot] = timetable[eachday][eachslot] + '/' + choice_lab
                                timetable[eachday][eachslot-1] = timetable[eachday][eachslot-1] + '/' + choice_lab
                                timetable[eachday][eachslot-2] = timetable[eachday][eachslot-2] + '/' + choice_lab
                        elif eachslot == 1:
                            if (timetable[eachday][eachslot+1] == timetable[eachday][eachslot]) and (timetable[eachday][eachslot-1] == timetable[eachday][eachslot]):
                                timetable[eachday][eachslot] = timetable[eachday][eachslot] + '/' + choice_lab
                                timetable[eachday][eachslot - 1] = timetable[eachday][eachslot - 1] + '/' + choice_lab
                                timetable[eachday][eachslot + 1] = timetable[eachday][eachslot + 1] + '/' + choice_lab
                            elif (timetable[eachday][eachslot+1] == timetable[eachday][eachslot]) and (timetable[eachday][eachslot+2] == timetable[eachday][eachslot]):
                                timetable[eachday][eachslot] = timetable[eachday][eachslot] + '/' + choice_lab
                                timetable[eachday][eachslot+1] = timetable[eachday][eachslot+1] + '/' + choice_lab
                                timetable[eachday][eachslot+2] = timetable[eachday][eachslot+2] + '/' + choice_lab
                        elif eachslot == 7:
                            if (timetable[eachday][eachslot+1] == timetable[eachday][eachslot]) and (timetable[eachday][eachslot-1] == timetable[eachday][eachslot]):
                                timetable[eachday][eachslot] = timetable[eachday][eachslot] + '/' + choice_lab
                                timetable[eachday][eachslot - 1] = timetable[eachday][eachslot - 1] + '/' + choice_lab
                                timetable[eachday][eachslot + 1] = timetable[eachday][eachslot + 1] + '/' + choice_lab
                            elif (timetable[eachday][eachslot-1] == timetable[eachday][eachslot]) and (timetable[eachday][eachslot-2] == timetable[eachday][eachslot]):
                                timetable[eachday][eachslot] = timetable[eachday][eachslot] + '/' + choice_lab
                                timetable[eachday][eachslot-1] = timetable[eachday][eachslot-1] + '/' + choice_lab
                                timetable[eachday][eachslot-2] = timetable[eachday][eachslot-2] + '/' + choice_lab
                        else:
                            if (timetable[eachday][eachslot+1] == timetable[eachday][eachslot]) and (timetable[eachday][eachslot-1] == timetable[eachday][eachslot]):
                                timetable[eachday][eachslot] = timetable[eachday][eachslot] + '/' + choice_lab
                                timetable[eachday][eachslot - 1] = timetable[eachday][eachslot - 1] + '/' + choice_lab
                                timetable[eachday][eachslot + 1] = timetable[eachday][eachslot + 1] + '/' + choice_lab
                            elif (timetable[eachday][eachslot+1] == timetable[eachday][eachslot]) and (timetable[eachday][eachslot+2] == timetable[eachday][eachslot]):
                                timetable[eachday][eachslot] = timetable[eachday][eachslot] + '/' + choice_lab
                                timetable[eachday][eachslot+1] = timetable[eachday][eachslot+1] + '/' + choice_lab
                                timetable[eachday][eachslot+2] = timetable[eachday][eachslot+2] + '/' + choice_lab
                            elif (timetable[eachday][eachslot-1] == timetable[eachday][eachslot]) and (timetable[eachday][eachslot-2] == timetable[eachday][eachslot]):
                                timetable[eachday][eachslot] = timetable[eachday][eachslot] + '/' + choice_lab
                                timetable[eachday][eachslot-1] = timetable[eachday][eachslot-1] + '/' + choice_lab
                                timetable[eachday][eachslot-2] = timetable[eachday][eachslot-2] + '/' + choice_lab



                    else:

                        freeclass = []
                        if class101[eachday][eachslot] == 0:
                            freeclass.append('class101')
                        if class102[eachday][eachslot] == 0:
                            freeclass.append('class102')
                        if class103[eachday][eachslot] == 0:
                            freeclass.append('class103')
                        if class104[eachday][eachslot] == 0:
                            freeclass.append('class104')
                        if class105[eachday][eachslot] == 0:
                            freeclass.append('class105')

                        choice_class = str(choice(freeclass))
                        if eachslot == 8:
                            if timetable[eachday][eachslot-1] == timetable[eachday][eachslot]:
                                timetable[eachday][eachslot] = timetable[eachday][eachslot] + '/' + choice_class
                                timetable[eachday][eachslot-1] = timetable[eachday][eachslot-1] + '/' + choice_class

                            else:
                                timetable[eachday][eachslot] = timetable[eachday][eachslot] + '/' + choice_class

                        elif eachslot == 0:
                            if timetable[eachday][eachslot+1] == timetable[eachday][eachslot]:
                                timetable[eachday][eachslot] = timetable[eachday][eachslot] + '/' + choice_class
                                timetable[eachday][eachslot + 1] = timetable[eachday][eachslot + 1] + '/' + choice_class

                            else:
                                timetable[eachday][eachslot] = timetable[eachday][eachslot] + '/' + choice_class
                        else:
                            if timetable[eachday][eachslot-1] == timetable[eachday][eachslot]:
                                timetable[eachday][eachslot] = timetable[eachday][eachslot] + '/' + choice_class
                                timetable[eachday][eachslot-1] = timetable[eachday][eachslot-1] + '/' + choice_class
                            elif timetable[eachday][eachslot+1] == timetable[eachday][eachslot]:
                                timetable[eachday][eachslot] = timetable[eachday][eachslot] + '/' + choice_class
                                timetable[eachday][eachslot + 1] = timetable[eachday][eachslot + 1] + '/' + choice_class

                            else:
                                timetable[eachday][eachslot] = timetable[eachday][eachslot] + '/' + choice_class
    return timetable


def timetable_for_single_teacher(teacher_name,timetable):
    teacher_timetable = timetable
    for each_day in range(len(teacher_timetable)):
        for eachs_slot in range(len(teacher_timetable[each_day])):
            if teacher_timetable[each_day][eachs_slot] != '0':
                split_with_slash = teacher_timetable[each_day][eachs_slot].split('/')
                if teacher_name in split_with_slash:
                    continue
                else:
                    teacher_timetable[each_day][eachs_slot] = 0
    return teacher_timetable




def main_screen():
    screen_main = Tk()


    screen_main.geometry("500x500")
    screen_main.title("UIT TIME TABLE SCHEDULER")
    screen_main.configure(background='light sky blue')
    heading = Label(screen_main, text="UIT TIME TABLE SCHEDULER", bg="steel blue", fg="black", width="500", height="3",font=("Lucida Console", 16))
    heading.pack()
    def courses_leftClick(event):
        screen_main.destroy()
        courses_screen()

    courses_button = Button(screen_main, text="Courses Entry", width="30", height="3",bg="light sky blue")
    courses_button.bind("<Button-1>", courses_leftClick)
    courses_button.place(x=150, y=250)

    def teachers_leftClick(event):
        screen_main.destroy()
        teachers_screeen()

    teachers_button = Button(screen_main, text="Teachers Entry", width="30", height="3",bg="light sky blue")
    teachers_button.bind("<Button-1>", teachers_leftClick)
    teachers_button.place(x=150, y=100)

    def timetable_leftClick(event):
        screen_main.destroy()
        timetable_screen()
    timetable_button = Button(screen_main, text="Create Time Table", width="30", height="3",bg="light sky blue")
    timetable_button.bind("<Button-1>",timetable_leftClick)
    timetable_button.place(x=150,y=400)



    screen_main.mainloop()



def courses_screen():
    screen_courses = Tk()

    def save_course(course_name_input,course_cdhr_input):
        if course_name_input.get() == '':
            messagebox.showinfo("Warning","Please enter course name!")
        elif course_cdhr_input.get() == 0:
            messagebox.showinfo("Warning", "Please enter course cdhr!")
        elif course_name_input.get() == '' and course_cdhr_input.get() == 0:
            messagebox.showinfo("Warning", "Please enter all fields!")
        else:
            course_name      = course_name_input.get()
            course_cdhr      = course_cdhr_input.get()

            courses_file = open("courses.txt",'r')
            courses_txt  = courses_file.readlines()
            courses_file.close()

            courses_txt.append(course_name+' '+str(course_cdhr)+'\n')

            courses_file = open("courses.txt",'w')
            courses_file.writelines(courses_txt)
            courses_file.close()

            course_name_entry.delete(0,END)
            course_cdhr_entry.delete(0,END)


    def save_lab(lab_name_input):
        if lab_name_input.get() == '':
            messagebox.showinfo('Warning', 'Please fill all the entries')
        else:
            lab_name = lab_name_input.get()

            courses_file = open("courses.txt", 'r')
            courses_txt = courses_file.readlines()
            courses_file.close()

            courses_txt.append(lab_name+'-lab'+' '+'3'+'\n')

            courses_file = open("courses.txt", 'w')
            courses_file.writelines(courses_txt)
            courses_file.close()

            lab_name_entry.delete(0,END)



    def delete():
        courses_file = open('courses.txt','w')
        courses_file.close()

    def view_courses():
        courses_list.delete(0,END)
        courses_file = open("courses.txt",'r')
        courses_txt = courses_file.readlines()
        courses_file.close()

        courses = {}
        for x in range(len(courses_txt)):
            splitted_line = courses_txt[x].split()
            course_name = splitted_line[0]
            course_cdhr = int(splitted_line[1])
            courses[course_name] = course_cdhr

        if courses_txt == '':
            messagebox.showinfo("Warning","No courses registered yet!")
        else:
            courses_list.insert(END,'{:^10}:{:^10}'.format('Course','CDHR'))
            courses_list.insert(END,'_____________________')
            for key,val in courses.items():
                courses_list.insert(END,'{:^10}:{:^10}'.format(key,val))








    screen_courses.geometry("500x500")
    screen_courses.title("UIT TIME TABLE SCHEDULER")
    screen_courses.configure(background="light sky blue")
    heading = Label(screen_courses, text="Courses Entry", bg="steel blue", fg="black", width="500", height="3",font=("Lucida Console", 12))
    heading.pack()
    my_font = font.Font(family="Monaco", size=12)
    courses_list = Listbox(screen_courses,font=my_font,width=20)
    courses_list.place(x=260,y=100)



    course_name_label = Label(screen_courses, text="Course Name :", bg="light sky blue")
    course_name_label.place(x=10,y=70)
    course_credit_hour= Label(screen_courses, text="Course CDHR :", bg="light sky blue")
    course_credit_hour.place(x=10,y=140)
    lab_name_label    = Label(screen_courses,text="Lab Name :", bg="light sky blue")
    lab_name_label.place(x=10,y=280)



    course_name_input = StringVar()
    course_cdhr_input = IntVar()
    lab_name_input    = StringVar()

    course_name_entry = Entry(screen_courses, textvariable=course_name_input, width="30")
    course_cdhr_entry = Entry(screen_courses, textvariable=course_cdhr_input, width="30")
    lab_name_entry    = Entry(screen_courses, textvariable=lab_name_input,width="30")


    course_name_entry.place(x=10, y=100)
    course_cdhr_entry.place(x=10, y=170)
    lab_name_entry.place(x=10,y=310)


    def add_course_leftClick(event):
        save_course(course_name_input,course_cdhr_input)
    add_course_button = Button(screen_courses,text="Add Course",bg="light sky blue")
    add_course_button.bind("<Button-1>", add_course_leftClick)
    add_course_button.place(x=10,y=210)

    def add_lab_leftClick(event):
        save_lab(lab_name_input)
    add_lab_button = Button(screen_courses,text="Add Lab",bg="light sky blue")
    add_lab_button.bind("<Button-1>",add_lab_leftClick)
    add_lab_button.place(x=10,y=340)


    def back_to_main_leftClick(event):
        screen_courses.destroy()
        timetable_file = open("timetable.txt", 'r')
        timetable_txt = timetable_file.readlines()
        timetable_file.close()
        if timetable_txt == []:
            main_screen()
        else:
            main_2_screen()
    back_to_main_button = Button(screen_courses,text="Main Menu",bg="light sky blue")
    back_to_main_button.bind("<Button-1>", back_to_main_leftClick)
    back_to_main_button.place(x=420,y=460)


    def delete_leftClick(event):
        delete()
    delete_button = Button(screen_courses,text="Delete all Courses",bg="light sky blue")
    delete_button.bind("<Button-1>",delete_leftClick)
    delete_button.place(x=10,y=460)



    def view_courses_leftClick(event):
        view_courses()
    view_courses_button = Button(screen_courses,text="View Courses",bg="light sky blue")
    view_courses_button.bind("<Button-1>",view_courses_leftClick)
    view_courses_button.place(x=260,y=70)

    screen_courses.mainloop()









def teachers_screeen():
    screen_teachers = Tk()

    def save_teacher(teacher_name_input,preferred_1_input,preferred_2_input,preferred_3_input):
        if teacher_name_input.get() == '':
            messagebox.showinfo("Warning","Enter Teacher Name")
        elif preferred_1_input.get() == '' and preferred_2_input.get() == '' and preferred_3_input.get() == '':
            messagebox.showinfo("Warning","Enter atleast 1 preferred course!")
        elif teacher_name_input.get() == '' and preferred_1_input.get() == '' and preferred_2_input.get() == '' and preferred_3_input.get() == '':
            messagebox.showinfo("Warning", "Enter all info!")
        else:

            teacher_name = teacher_name_input.get()
            preferred_1  = preferred_1_input.get()
            preferred_2  = preferred_2_input.get()
            preferred_3  = preferred_3_input.get()
            teacher_name = teacher_name.lower()
            preferred_1 = preferred_1.lower()
            preferred_2 = preferred_2.lower()
            preferred_3 = preferred_3.lower()


            teachers_file = open('teachers.txt','r')
            teachers_txt = teachers_file.readlines()
            teachers_file.close()

            teachers_txt.append(teacher_name+' '+preferred_1+' '+preferred_2+' '+preferred_3+'\n')

            teachers_file = open('teachers.txt','w')
            teachers_file.writelines(teachers_txt)
            teachers_file.close()

            teacher_name_entry.delete(0,END)
            preferred_1_entry.delete(0,END)
            preferred_2_entry.delete(0,END)
            preferred_3_entry.delete(0,END)


    def delete():
        teachers_file = open('teachers.txt','w')
        teachers_file.close()

    def view_teachers():
        teachers_list.delete(0, END)
        teachers_file = open("teachers.txt", 'r')
        teachers_txt = teachers_file.readlines()
        teachers_file.close()
        teachers = {}

        for y in range(len(teachers_txt)):
            pref = []
            splitted_line = teachers_txt[y].split()
            teacher_name = splitted_line[0]
            pref.append(splitted_line[1])
            if len(splitted_line) == 3:
                pref.append(splitted_line[2])
            elif len(splitted_line) == 4:
                pref.append(splitted_line[2])
                pref.append(splitted_line[3])
            teachers[teacher_name] = pref

        if teachers_txt == '':
            messagebox.showinfo("Warning", "No teachers registered yet!")
        else:
            teachers_list.insert(END,'{:^10}:{:^10}'.format('Teacher','Pref.'))
            teachers_list.insert(END, "_____________________")
            for key,val in teachers.items():
                teachers_list.insert(END,"{:<10}:{:<10}".format(key.title(),str(val)))





    screen_teachers.geometry("500x500")
    screen_teachers.title("UIT TIME TABLE SCHEDULER")
    screen_teachers.configure(background="light sky blue")
    heading = Label(screen_teachers, text="Teachers Entry", bg="steel blue", fg="black", width="500", height="3",font=("Lucida Console", 12))
    heading.pack()

    my_font = font.Font(family="Monaco", size=12)

    teachers_list = Listbox(screen_teachers,font = my_font,width=20)
    teachers_list.place(x=260, y=100)

    teacher_name_label = Label(screen_teachers,text='Teachers First Name:', bg="light sky blue")
    preferred_1_label  = Label(screen_teachers,text="Most Preferred Course:", bg="light sky blue")
    preferred_2_label  = Label(screen_teachers,text="Average Preferred Course:", bg="light sky blue")
    preferred_3_label  = Label(screen_teachers,text="Least Preferred Course:", bg="light sky blue")

    teacher_name_label.place(x=10,y=70)
    preferred_1_label.place(x=10,y=140)
    preferred_2_label.place(x=10,y=210)
    preferred_3_label.place(x=10, y=280)

    teacher_name_input = StringVar()
    preferred_1_input = StringVar()
    preferred_2_input = StringVar()
    preferred_3_input = StringVar()

    teacher_name_entry = Entry(screen_teachers,text=teacher_name_input,width="30")
    preferred_1_entry  = Entry(screen_teachers,text=preferred_1_input,width="30")
    preferred_2_entry  = Entry(screen_teachers,text=preferred_2_input,width="30")
    preferred_3_entry  = Entry(screen_teachers,text=preferred_3_input,width="30")

    teacher_name_entry.place(x=10,y=105)
    preferred_1_entry.place(x=10, y=175)
    preferred_2_entry.place(x=10, y=245)
    preferred_3_entry.place(x=10, y=325)


    teacher_not_available_day_label = Label(screen_teachers,text='If teacher not available',bg="light sky blue")
    teacher_not_available_day_label.place(x=260,y=300)

    teacher_name_available_label = Label(screen_teachers,text='Select teacher:',bg="light sky blue")
    teacher_name_available_label.place(x=260,y=330)

    teachers_file = open("teachers.txt",'r')
    teachers_txt = teachers_file.readlines()
    teachers_file.close()
    teachers = {}

    for y in range(len(teachers_txt)):
        pref = []
        splitted_line = teachers_txt[y].split()
        teacher_name = splitted_line[0]
        pref.append(splitted_line[1])
        if len(splitted_line) == 3:
            pref.append(splitted_line[2])
        elif len(splitted_line) == 4:
            pref.append(splitted_line[2])
            pref.append(splitted_line[3])
        teachers[teacher_name] = pref

    teachers_avb_list = list(teachers.keys())

    teacher_avb_name = StringVar()

    teacher_avb_name_option = OptionMenu(screen_teachers, teacher_avb_name, *teachers_avb_list)
    teacher_avb_name_option.place(x=260,y=350)

    teacher_avb_day_label = Label(screen_teachers,text="Select Day:",bg="light sky blue")
    teacher_avb_day_label.place(x=350,y=330)

    teacher_avb_day  = StringVar()
    list_of_days = ['Mon','Tue','Wed','Thu','Fri']

    teacher_avb_day_option = OptionMenu(screen_teachers, teacher_avb_day, *list_of_days)
    teacher_avb_day_option.place(x=350,y=350)


    def save_teacher_avb(teacher_avb_name,teacher_avb_day):

        if teacher_avb_name.get() == '' or teacher_avb_day.get() == '':
            messagebox.showinfo("Warning","Select all fields")
        else:
            teacher_n = teacher_avb_name.get()
            teacher_d = teacher_avb_day.get()
            dict_of_days = {'Mon':0, 'Tue':1, 'Wed':2, 'Thu':3, 'Fri':4}
            teacher_d = dict_of_days[teacher_d]

            teacher_avb_file = open('teacher_avb.txt','r')
            teacher_avb_txt = teacher_avb_file.readlines()
            teacher_avb_file.close()

            teacher_avb_text = str(teacher_n)+' '+str(teacher_d)+'\n'
            teacher_avb_txt.append(teacher_avb_text)

            teacher_avb_file = open('teacher_avb.txt', 'w')
            teacher_avb_file.writelines(teacher_avb_txt)
            teacher_avb_file.close()


    def confirm_avb_day_leftClick(event):
        save_teacher_avb(teacher_avb_name,teacher_avb_day)


    confirm_avb_day_button = Button(screen_teachers,text="Confirm",bg="light sky blue",width=30)
    confirm_avb_day_button.bind("<Button-1>",confirm_avb_day_leftClick)
    confirm_avb_day_button.place(x=260,y=380)

    def delete_all_avb_leftClick(event):
        teacher_avb_file = open('teacher_avb.txt', 'w')
        teacher_avb_file.close()

    delete_all_avb_button = Button(screen_teachers,text="Delete all availabilities",bg="light sky blue",width=30)
    delete_all_avb_button.bind("<Button-1>",delete_all_avb_leftClick)
    delete_all_avb_button.place(x=260,y=410)







    def add_teacher_leftClick(event):
        save_teacher(teacher_name_input,preferred_1_input,preferred_2_input,preferred_3_input)

    add_teacher_button = Button(screen_teachers,text="Add Teacher",bg="light sky blue")
    add_teacher_button.bind("<Button-1>",add_teacher_leftClick)
    add_teacher_button.place(x=10, y=360)

    def delete_leftClick(event):
        delete()
    delete_button = Button(screen_teachers,text="Delete all Teachers",bg="light sky blue")
    delete_button.bind("<Button-1>",delete_leftClick)
    delete_button.place(x=10,y=460)





    def back_to_main_leftClick(event):
        screen_teachers.destroy()
        timetable_file = open("timetable.txt", 'r')
        timetable_txt = timetable_file.readlines()
        timetable_file.close()
        if timetable_txt == []:
            main_screen()
        else:
            main_2_screen()
    back_to_main_button = Button(screen_teachers,text="Main Menu",bg="light sky blue")
    back_to_main_button.bind("<Button-1>", back_to_main_leftClick)
    back_to_main_button.place(x=420,y=460)

    def view_teachers_leftClick(event):
        view_teachers()

    view_teachers_button = Button(screen_teachers, text="View Teachers",bg="light sky blue")
    view_teachers_button.bind("<Button-1>", view_teachers_leftClick)
    view_teachers_button.place(x=260, y=70)


    screen_teachers.mainloop()

def timetable_screen():
    screen_timetable = Tk()

    courses = {}
    teachers= {}
    availability = {}

    courses_file = open('courses.txt','r')
    courses_txt = courses_file.readlines()
    courses_file.close()

    teachers_file= open("teachers.txt",'r')
    teachers_txt = teachers_file.readlines()
    teachers_file.close()

    teacher_avb_file = open("teacher_avb.txt",'r')
    teacher_avb_txt  = teacher_avb_file.readlines()
    teacher_avb_file.close()

    for x in range(len(teacher_avb_txt)):
        splitted_line = teacher_avb_txt[x].split()
        t_name = splitted_line[0]
        t_day  = splitted_line[1]
        availability[t_name] = int(t_day)




    for x in range(len(courses_txt)):
        splitted_line = courses_txt[x].split()
        course_name = splitted_line[0]
        course_cdhr = int(splitted_line[1])
        courses[course_name] = course_cdhr

    for y in range(len(teachers_txt)):
        pref = []
        splitted_line = teachers_txt[y].split()
        teacher_name = splitted_line[0]
        pref.append(splitted_line[1])
        if len(splitted_line) == 3:
            pref.append(splitted_line[2])
        elif len(splitted_line) == 4:
            pref.append(splitted_line[2])
            pref.append(splitted_line[3])
        teachers[teacher_name] = pref


    def create_new(teachers,courses,availability):



        if courses == {} and teachers == {}:
            messagebox.showinfo("Warning","No Courses and Teachers Registered")
        elif courses == {}:
            messagebox.showinfo("Warning", "No Courses Registered")
        elif teachers == {}:
            messagebox.showinfo("Warning", "No Teachers Registered")
        else:
            t_c_pair = make_teacher_course_pair(teachers, courses)
            timetable = assign_slots(t_c_pair, courses,availability)
            timetable = assign_classes(timetable)
            print_timetable(timetable)

        label_mon_1 = Label(screen_timetable,text=timetable[0][0],justify=CENTER,bg="light sky blue",width=15)
        label_mon_2 = Label(screen_timetable,text=timetable[0][1],justify=CENTER,bg="light sky blue",width=15)
        label_mon_3 = Label(screen_timetable,text=timetable[0][2],justify=CENTER,bg="light sky blue",width=15)
        label_mon_4 = Label(screen_timetable,text=timetable[0][3],justify=CENTER,bg="light sky blue",width=15)
        label_mon_5 = Label(screen_timetable,text=timetable[0][4],justify=CENTER,bg="light sky blue",width=15)
        label_mon_6 = Label(screen_timetable,text=timetable[0][5],justify=CENTER,bg="light sky blue",width=15)
        label_mon_7 = Label(screen_timetable,text=timetable[0][6],justify=CENTER,bg="light sky blue",width=15)
        label_mon_8 = Label(screen_timetable,text=timetable[0][7],justify=CENTER,bg="light sky blue",width=15)
        label_mon_9 = Label(screen_timetable,text=timetable[0][8],justify=CENTER,bg="light sky blue",width=15)

        label_mon_1.place(x=100, y=80)
        label_mon_2.place(x=220, y=80)
        label_mon_3.place(x=340, y=80)
        label_mon_4.place(x=460, y=80)
        label_mon_5.place(x=580, y=80)
        label_mon_6.place(x=700, y=80)
        label_mon_7.place(x=820, y=80)
        label_mon_8.place(x=940, y=80)
        label_mon_9.place(x=1060, y=80)


        label_tue_1 = Label(screen_timetable, text=timetable[1][0],justify=CENTER,bg="light sky blue",width=15)
        label_tue_2 = Label(screen_timetable, text=timetable[1][1], justify=CENTER, bg="light sky blue", width=15)
        label_tue_3 = Label(screen_timetable, text=timetable[1][2], justify=CENTER, bg="light sky blue", width=15)
        label_tue_4 = Label(screen_timetable, text=timetable[1][3], justify=CENTER, bg="light sky blue", width=15)
        label_tue_5 = Label(screen_timetable, text=timetable[1][4], justify=CENTER, bg="light sky blue", width=15)
        label_tue_6 = Label(screen_timetable, text=timetable[1][5], justify=CENTER, bg="light sky blue", width=15)
        label_tue_7 = Label(screen_timetable, text=timetable[1][6], justify=CENTER, bg="light sky blue", width=15)
        label_tue_8 = Label(screen_timetable, text=timetable[1][7], justify=CENTER, bg="light sky blue", width=15)
        label_tue_9 = Label(screen_timetable, text=timetable[1][8], justify=CENTER, bg="light sky blue", width=15)

        label_tue_1.place(x=100, y=160)
        label_tue_2.place(x=220, y=160)
        label_tue_3.place(x=340, y=160)
        label_tue_4.place(x=460, y=160)
        label_tue_5.place(x=580, y=160)
        label_tue_6.place(x=700, y=160)
        label_tue_7.place(x=820, y=160)
        label_tue_8.place(x=940, y=160)
        label_tue_9.place(x=1060, y=160)

        label_wed_1 = Label(screen_timetable, text=timetable[2][0],justify=CENTER,bg="light sky blue",width=15)
        label_wed_2 = Label(screen_timetable, text=timetable[2][1], justify=CENTER, bg="light sky blue", width=15)
        label_wed_3 = Label(screen_timetable, text=timetable[2][2], justify=CENTER, bg="light sky blue", width=15)
        label_wed_4 = Label(screen_timetable, text=timetable[2][3], justify=CENTER, bg="light sky blue", width=15)
        label_wed_5 = Label(screen_timetable, text=timetable[2][4], justify=CENTER, bg="light sky blue", width=15)
        label_wed_6 = Label(screen_timetable, text=timetable[2][5], justify=CENTER, bg="light sky blue", width=15)
        label_wed_7 = Label(screen_timetable, text=timetable[2][6], justify=CENTER, bg="light sky blue", width=15)
        label_wed_8 = Label(screen_timetable, text=timetable[2][7], justify=CENTER, bg="light sky blue", width=15)
        label_wed_9 = Label(screen_timetable, text=timetable[2][8], justify=CENTER, bg="light sky blue", width=15)

        label_wed_1.place(x=100, y=240)
        label_wed_2.place(x=220, y=240)
        label_wed_3.place(x=340, y=240)
        label_wed_4.place(x=460, y=240)
        label_wed_5.place(x=580, y=240)
        label_wed_6.place(x=700, y=240)
        label_wed_7.place(x=820, y=240)
        label_wed_8.place(x=940, y=240)
        label_wed_9.place(x=1060, y=240)

        label_thu_1 = Label(screen_timetable, text=timetable[3][0],justify=CENTER,bg="light sky blue",width=15)
        label_thu_2 = Label(screen_timetable, text=timetable[3][1], justify=CENTER, bg="light sky blue", width=15)
        label_thu_3 = Label(screen_timetable, text=timetable[3][2], justify=CENTER, bg="light sky blue", width=15)
        label_thu_4 = Label(screen_timetable, text=timetable[3][3], justify=CENTER, bg="light sky blue", width=15)
        label_thu_5 = Label(screen_timetable, text=timetable[3][4], justify=CENTER, bg="light sky blue", width=15)
        label_thu_6 = Label(screen_timetable, text=timetable[3][5], justify=CENTER, bg="light sky blue", width=15)
        label_thu_7 = Label(screen_timetable, text=timetable[3][6], justify=CENTER, bg="light sky blue", width=15)
        label_thu_8 = Label(screen_timetable, text=timetable[3][7], justify=CENTER, bg="light sky blue", width=15)
        label_thu_9 = Label(screen_timetable, text=timetable[3][8], justify=CENTER, bg="light sky blue", width=15)

        label_thu_1.place(x=100, y=320)
        label_thu_2.place(x=220, y=320)
        label_thu_3.place(x=340, y=320)
        label_thu_4.place(x=460, y=320)
        label_thu_5.place(x=580, y=320)
        label_thu_6.place(x=700, y=320)
        label_thu_7.place(x=820, y=320)
        label_thu_8.place(x=940, y=320)
        label_thu_9.place(x=1060, y=320)

        label_fri_1 = Label(screen_timetable, text=timetable[4][0],justify=CENTER,bg="light sky blue",width=15)
        label_fri_2 = Label(screen_timetable, text=timetable[4][1], justify=CENTER, bg="light sky blue", width=15)
        label_fri_3 = Label(screen_timetable, text=timetable[4][2], justify=CENTER, bg="light sky blue", width=15)
        label_fri_4 = Label(screen_timetable, text=timetable[4][3], justify=CENTER, bg="light sky blue", width=15)
        label_fri_5 = Label(screen_timetable, text=timetable[4][4], justify=CENTER, bg="light sky blue", width=15)
        label_fri_6 = Label(screen_timetable, text=timetable[4][5], justify=CENTER, bg="light sky blue", width=15)
        label_fri_7 = Label(screen_timetable, text=timetable[4][6], justify=CENTER, bg="light sky blue", width=15)
        label_fri_8 = Label(screen_timetable, text=timetable[4][7], justify=CENTER, bg="light sky blue", width=15)
        label_fri_9 = Label(screen_timetable, text=timetable[4][8], justify=CENTER, bg="light sky blue", width=15)

        label_fri_1.place(x=100, y=400)
        label_fri_2.place(x=220, y=400)
        label_fri_3.place(x=340, y=400)
        label_fri_4.place(x=460, y=400)
        label_fri_5.place(x=580, y=400)
        label_fri_6.place(x=700, y=400)
        label_fri_7.place(x=820, y=400)
        label_fri_8.place(x=940, y=400)
        label_fri_9.place(x=1060, y=400)

        def save_timetable(timetable):

            timetable_file = open('timetable.txt', 'w')
            timetable_file.close()

            timetable_txt = ''

            for each_day in range(len(timetable)):
                for each_slot in range(len(timetable[each_day])):
                    timetable_txt = timetable_txt + str(timetable[each_day][each_slot]) + ' '
                timetable_txt = timetable_txt+'\n'
            timetable_file = open('timetable.txt', 'w')
            timetable_file.writelines(timetable_txt)
            timetable_file.close()

            def main_2_leftClick(event):
                screen_timetable.destroy()
                main_2_screen()

            main_2_button = Button(screen_timetable, text="Main Menu")
            main_2_button.bind("<Button-1>", main_2_leftClick)
            main_2_button.place(x=1130, y=474)




        def save_timetable_leftClick(event):
            save_timetable(timetable)

        save_timetable_button = Button(screen_timetable, text="Save Timetable")
        save_timetable_button.bind("<Button-1>", save_timetable_leftClick)
        save_timetable_button.place(x=100, y=474)


    screen_timetable.geometry("1200x500")
    screen_timetable.title("UIT TIME TABLE SCHEDULER")
    screen_timetable.configure(background="light sky blue")
    heading = Label(screen_timetable, text="Timetable", bg="steel blue", fg="black", width="500", height="3",font=("Lucida Console", 12))
    heading.pack()

    label_mon = Label(screen_timetable,text ="Mon",justify=CENTER,bg="light sky blue")
    label_tue = Label(screen_timetable,text ="Tue",justify=CENTER,bg="light sky blue")
    label_wed = Label(screen_timetable,text ="Wed",justify=CENTER,bg="light sky blue")
    label_thu = Label(screen_timetable,text ="Thu",justify=CENTER,bg="light sky blue")
    label_fri = Label(screen_timetable,text ="Fri",justify=CENTER,bg="light sky blue")
    label_8   = Label(screen_timetable,text ="8-9",justify=CENTER,bg="light sky blue")
    label_9   = Label(screen_timetable,text ="9-10",justify=CENTER,bg="light sky blue")
    label_10  = Label(screen_timetable,text ="10-11",justify=CENTER,bg="light sky blue")
    label_11  = Label(screen_timetable,text ="11-12",justify=CENTER,bg="light sky blue")
    label_12  = Label(screen_timetable,text ="12-1",justify=CENTER,bg="light sky blue")
    label_1   = Label(screen_timetable,text ="1-2",justify=CENTER,bg="light sky blue")
    label_2   = Label(screen_timetable,text ="2-3",justify=CENTER,bg="light sky blue")
    label_3   = Label(screen_timetable,text ="3-4",justify=CENTER,bg="light sky blue")
    label_4   = Label(screen_timetable,text ="4-5",justify=CENTER,bg="light sky blue")

    label_mon.place(x=10, y=80)
    label_tue.place(x=10, y=160)
    label_wed.place(x=10, y=240)
    label_thu.place(x=10, y=320)
    label_fri.place(x=10, y=400)
    label_8.place(x=150, y=60)
    label_9.place(x=270, y=60)
    label_10.place(x=390, y=60)
    label_11.place(x=510, y=60)
    label_12.place(x=630, y=60)
    label_1.place(x=750, y=60)
    label_2.place(x=860, y=60)
    label_3.place(x=990, y=60)
    label_4.place(x=1110, y=60)











    def create_new_leftClick(event):
        create_new(teachers,courses,availability)

    create_new_button = Button(screen_timetable,text="Create New")
    create_new_button.bind("<Button-1>",create_new_leftClick)
    create_new_button.place(x=5,y=474)

    def main_leftClick(event):
        screen_timetable.destroy()
        timetable_file = open("timetable.txt", 'r')
        timetable_txt = timetable_file.readlines()
        timetable_file.close()
        if timetable_txt == []:
            main_screen()
        else:
            main_2_screen()
    main_button = Button(screen_timetable,text="Main Menu")
    main_button.bind("<Button-1>",main_leftClick)
    main_button.place(x=1130,y=474)





    screen_timetable.mainloop()


def main_2_screen():
    screen_main2 = Tk()

    screen_main2.geometry("500x500")
    screen_main2.title("UIT TIME TABLE SCHEDULER")
    screen_main2.configure(background='light sky blue')
    heading = Label(screen_main2, text="UIT TIME TABLE SCHEDULER", bg="steel blue", fg="black", width="500", height="3",
                    font=("Lucida Console", 16))
    heading.pack()


    def courses_leftClick(event):
        screen_main2.destroy()
        courses_screen()

    courses_button = Button(screen_main2, text="Courses Entry", width="30", height="3",bg="light sky blue")
    courses_button.bind("<Button-1>", courses_leftClick)
    courses_button.place(x=150, y=250)

    def teachers_leftClick(event):
        screen_main2.destroy()
        teachers_screeen()

    teachers_button = Button(screen_main2, text="Teachers Entry", width="30", height="3",bg="light sky blue")
    teachers_button.bind("<Button-1>", teachers_leftClick)
    teachers_button.place(x=150, y=100)

    def timetable_leftClick(event):
        screen_main2.destroy()
        timetable_screen()

    timetable_button = Button(screen_main2, text="Create Time Table", width="30", height="3",bg="light sky blue")
    timetable_button.bind("<Button-1>", timetable_leftClick)
    timetable_button.place(x=30, y=400)


    def view_timetable_leftClick(event):

        teachers_file = open("teachers.txt",'r')
        teachers_txt = teachers_file.readlines()
        teachers_file.close()
        if teachers_txt == []:
            messagebox.showinfo("Warning","There are no teachers registered! Please enter teachers first.")
        else:
            screen_main2.destroy()
            view_timetable_screen()

    view_timetable_button = Button(screen_main2,text="View Time Table", width="30", height="3",bg="light sky blue")
    view_timetable_button.bind("<Button-1>",view_timetable_leftClick)
    view_timetable_button.place(x=270, y=400)

    screen_main2.mainloop()

def view_timetable_screen():

    timetable_file = open("timetable.txt",'r')
    timetable_txt = timetable_file.readlines()
    timetable_file.close()

    timetable= []

    for each_line in timetable_txt:
        splitted_line = each_line.split()
        timetable.append(splitted_line)

    screen_view = Tk()

    screen_view.geometry("1200x500")
    screen_view.title("UIT TIME TABLE SCHEDULER")
    screen_view.configure(background="light sky blue")
    heading = Label(screen_view, text="Timetable View", bg="steel blue", fg="black", width="500", height="3",
                    font=("Lucida Console", 12))
    heading.pack()

    label_mon = Label(screen_view, text="Mon",bg="light sky blue", justify=CENTER)
    label_tue = Label(screen_view, text="Tue",bg="light sky blue", justify=CENTER)
    label_wed = Label(screen_view, text="Wed",bg="light sky blue", justify=CENTER)
    label_thu = Label(screen_view, text="Thu",bg="light sky blue", justify=CENTER)
    label_fri = Label(screen_view, text="Fri",bg="light sky blue", justify=CENTER)
    label_8 = Label(screen_view, text="8-9",bg="light sky blue", justify=CENTER)
    label_9 = Label(screen_view, text="9-10",bg="light sky blue", justify=CENTER)
    label_10 = Label(screen_view, text="10-11",bg="light sky blue", justify=CENTER)
    label_11 = Label(screen_view, text="11-12",bg="light sky blue", justify=CENTER)
    label_12 = Label(screen_view, text="12-1",bg="light sky blue", justify=CENTER)
    label_1 = Label(screen_view, text="1-2",bg="light sky blue", justify=CENTER)
    label_2 = Label(screen_view, text="2-3",bg="light sky blue", justify=CENTER)
    label_3 = Label(screen_view, text="3-4",bg="light sky blue", justify=CENTER)
    label_4 = Label(screen_view, text="4-5",bg="light sky blue", justify=CENTER)

    label_mon.place(x=10, y=80)
    label_tue.place(x=10, y=160)
    label_wed.place(x=10, y=240)
    label_thu.place(x=10, y=320)
    label_fri.place(x=10, y=400)
    label_8.place(x=150, y=60)
    label_9.place(x=270, y=60)
    label_10.place(x=390, y=60)
    label_11.place(x=510, y=60)
    label_12.place(x=630, y=60)
    label_1.place(x=750, y=60)
    label_2.place(x=860, y=60)
    label_3.place(x=990, y=60)
    label_4.place(x=1110, y=60)

    label_mon_1 = Label(screen_view, text=timetable[0][0], justify=CENTER, bg="light sky blue", width=15)
    label_mon_2 = Label(screen_view, text=timetable[0][1], justify=CENTER, bg="light sky blue", width=15)
    label_mon_3 = Label(screen_view, text=timetable[0][2], justify=CENTER, bg="light sky blue", width=15)
    label_mon_4 = Label(screen_view, text=timetable[0][3], justify=CENTER, bg="light sky blue", width=15)
    label_mon_5 = Label(screen_view, text=timetable[0][4], justify=CENTER, bg="light sky blue", width=15)
    label_mon_6 = Label(screen_view, text=timetable[0][5], justify=CENTER, bg="light sky blue", width=15)
    label_mon_7 = Label(screen_view, text=timetable[0][6], justify=CENTER, bg="light sky blue", width=15)
    label_mon_8 = Label(screen_view, text=timetable[0][7], justify=CENTER, bg="light sky blue", width=15)
    label_mon_9 = Label(screen_view, text=timetable[0][8], justify=CENTER, bg="light sky blue", width=15)

    label_mon_1.place(x=100, y=80)
    label_mon_2.place(x=220, y=80)
    label_mon_3.place(x=340, y=80)
    label_mon_4.place(x=460, y=80)
    label_mon_5.place(x=580, y=80)
    label_mon_6.place(x=700, y=80)
    label_mon_7.place(x=820, y=80)
    label_mon_8.place(x=940, y=80)
    label_mon_9.place(x=1060, y=80)

    label_tue_1 = Label(screen_view, text=timetable[1][0], justify=CENTER, bg="light sky blue", width=15)
    label_tue_2 = Label(screen_view, text=timetable[1][1], justify=CENTER, bg="light sky blue", width=15)
    label_tue_3 = Label(screen_view, text=timetable[1][2], justify=CENTER, bg="light sky blue", width=15)
    label_tue_4 = Label(screen_view, text=timetable[1][3], justify=CENTER, bg="light sky blue", width=15)
    label_tue_5 = Label(screen_view, text=timetable[1][4], justify=CENTER, bg="light sky blue", width=15)
    label_tue_6 = Label(screen_view, text=timetable[1][5], justify=CENTER, bg="light sky blue", width=15)
    label_tue_7 = Label(screen_view, text=timetable[1][6], justify=CENTER, bg="light sky blue", width=15)
    label_tue_8 = Label(screen_view, text=timetable[1][7], justify=CENTER, bg="light sky blue", width=15)
    label_tue_9 = Label(screen_view, text=timetable[1][8], justify=CENTER, bg="light sky blue", width=15)

    label_tue_1.place(x=100, y=160)
    label_tue_2.place(x=220, y=160)
    label_tue_3.place(x=340, y=160)
    label_tue_4.place(x=460, y=160)
    label_tue_5.place(x=580, y=160)
    label_tue_6.place(x=700, y=160)
    label_tue_7.place(x=820, y=160)
    label_tue_8.place(x=940, y=160)
    label_tue_9.place(x=1060, y=160)

    label_wed_1 = Label(screen_view, text=timetable[2][0], justify=CENTER, bg="light sky blue", width=15)
    label_wed_2 = Label(screen_view, text=timetable[2][1], justify=CENTER, bg="light sky blue", width=15)
    label_wed_3 = Label(screen_view, text=timetable[2][2], justify=CENTER, bg="light sky blue", width=15)
    label_wed_4 = Label(screen_view, text=timetable[2][3], justify=CENTER, bg="light sky blue", width=15)
    label_wed_5 = Label(screen_view, text=timetable[2][4], justify=CENTER, bg="light sky blue", width=15)
    label_wed_6 = Label(screen_view, text=timetable[2][5], justify=CENTER, bg="light sky blue", width=15)
    label_wed_7 = Label(screen_view, text=timetable[2][6], justify=CENTER, bg="light sky blue", width=15)
    label_wed_8 = Label(screen_view, text=timetable[2][7], justify=CENTER, bg="light sky blue", width=15)
    label_wed_9 = Label(screen_view, text=timetable[2][8], justify=CENTER, bg="light sky blue", width=15)

    label_wed_1.place(x=100, y=240)
    label_wed_2.place(x=220, y=240)
    label_wed_3.place(x=340, y=240)
    label_wed_4.place(x=460, y=240)
    label_wed_5.place(x=580, y=240)
    label_wed_6.place(x=700, y=240)
    label_wed_7.place(x=820, y=240)
    label_wed_8.place(x=940, y=240)
    label_wed_9.place(x=1060, y=240)

    label_thu_1 = Label(screen_view, text=timetable[3][0], justify=CENTER, bg="light sky blue", width=15)
    label_thu_2 = Label(screen_view, text=timetable[3][1], justify=CENTER, bg="light sky blue", width=15)
    label_thu_3 = Label(screen_view, text=timetable[3][2], justify=CENTER, bg="light sky blue", width=15)
    label_thu_4 = Label(screen_view, text=timetable[3][3], justify=CENTER, bg="light sky blue", width=15)
    label_thu_5 = Label(screen_view, text=timetable[3][4], justify=CENTER, bg="light sky blue", width=15)
    label_thu_6 = Label(screen_view, text=timetable[3][5], justify=CENTER, bg="light sky blue", width=15)
    label_thu_7 = Label(screen_view, text=timetable[3][6], justify=CENTER, bg="light sky blue", width=15)
    label_thu_8 = Label(screen_view, text=timetable[3][7], justify=CENTER, bg="light sky blue", width=15)
    label_thu_9 = Label(screen_view, text=timetable[3][8], justify=CENTER, bg="light sky blue", width=15)

    label_thu_1.place(x=100, y=320)
    label_thu_2.place(x=220, y=320)
    label_thu_3.place(x=340, y=320)
    label_thu_4.place(x=460, y=320)
    label_thu_5.place(x=580, y=320)
    label_thu_6.place(x=700, y=320)
    label_thu_7.place(x=820, y=320)
    label_thu_8.place(x=940, y=320)
    label_thu_9.place(x=1060, y=320)

    label_fri_1 = Label(screen_view, text=timetable[4][0], justify=CENTER, bg="light sky blue", width=15)
    label_fri_2 = Label(screen_view, text=timetable[4][1], justify=CENTER, bg="light sky blue", width=15)
    label_fri_3 = Label(screen_view, text=timetable[4][2], justify=CENTER, bg="light sky blue", width=15)
    label_fri_4 = Label(screen_view, text=timetable[4][3], justify=CENTER, bg="light sky blue", width=15)
    label_fri_5 = Label(screen_view, text=timetable[4][4], justify=CENTER, bg="light sky blue", width=15)
    label_fri_6 = Label(screen_view, text=timetable[4][5], justify=CENTER, bg="light sky blue", width=15)
    label_fri_7 = Label(screen_view, text=timetable[4][6], justify=CENTER, bg="light sky blue", width=15)
    label_fri_8 = Label(screen_view, text=timetable[4][7], justify=CENTER, bg="light sky blue", width=15)
    label_fri_9 = Label(screen_view, text=timetable[4][8], justify=CENTER, bg="light sky blue", width=15)

    label_fri_1.place(x=100, y=400)
    label_fri_2.place(x=220, y=400)
    label_fri_3.place(x=340, y=400)
    label_fri_4.place(x=460, y=400)
    label_fri_5.place(x=580, y=400)
    label_fri_6.place(x=700, y=400)
    label_fri_7.place(x=820, y=400)
    label_fri_8.place(x=940, y=400)
    label_fri_9.place(x=1060, y=400)

    view_option_label = Label(screen_view,text="Choose teacher view :",bg="light sky blue")
    view_option_label.place(x=5,y=450)

    teachers_file = open("teachers.txt", 'r')
    teachers_txt = teachers_file.readlines()
    teachers_file.close()

    teachers = {}

    for y in range(len(teachers_txt)):
        pref = []
        splitted_line = teachers_txt[y].split()
        teacher_name = splitted_line[0]
        pref.append(splitted_line[1])
        if len(splitted_line) == 3:
            pref.append(splitted_line[2])
        elif len(splitted_line) == 4:
            pref.append(splitted_line[2])
            pref.append(splitted_line[3])
        teachers[teacher_name] = pref


    teachers_names_list = list(teachers.keys())
    option = StringVar()
    view_option_menu= OptionMenu(screen_view,option, *teachers_names_list)
    view_option_menu.place(x=5,y=474)





    def view_option_button_leftClick(event):
        timetable_file = open("timetable.txt", 'r')
        timetable_txt = timetable_file.readlines()
        timetable_file.close()

        timetable = []

        for each_line in timetable_txt:
            splitted_line = each_line.split()
            timetable.append(splitted_line)

        teacher_name = option.get()
        timetable = timetable_for_single_teacher(teacher_name,timetable)
        print_timetable(timetable)

        label_mon = Label(screen_view, text="Mon", justify=CENTER,bg="light sky blue")
        label_tue = Label(screen_view, text="Tue", justify=CENTER,bg="light sky blue")
        label_wed = Label(screen_view, text="Wed", justify=CENTER,bg="light sky blue")
        label_thu = Label(screen_view, text="Thu", justify=CENTER,bg="light sky blue")
        label_fri = Label(screen_view, text="Fri", justify=CENTER,bg="light sky blue")
        label_8 = Label(screen_view, text="8-9", justify=CENTER,bg="light sky blue")
        label_9 = Label(screen_view, text="9-10", justify=CENTER,bg="light sky blue")
        label_10 = Label(screen_view, text="10-11", justify=CENTER,bg="light sky blue")
        label_11 = Label(screen_view, text="11-12", justify=CENTER,bg="light sky blue")
        label_12 = Label(screen_view, text="12-1", justify=CENTER,bg="light sky blue")
        label_1 = Label(screen_view, text="1-2", justify=CENTER,bg="light sky blue")
        label_2 = Label(screen_view, text="2-3", justify=CENTER,bg="light sky blue")
        label_3 = Label(screen_view, text="3-4", justify=CENTER,bg="light sky blue")
        label_4 = Label(screen_view, text="4-5", justify=CENTER,bg="light sky blue")

        label_mon.place(x=10, y=80)
        label_tue.place(x=10, y=160)
        label_wed.place(x=10, y=240)
        label_thu.place(x=10, y=320)
        label_fri.place(x=10, y=400)
        label_8.place(x=150, y=60)
        label_9.place(x=270, y=60)
        label_10.place(x=390, y=60)
        label_11.place(x=510, y=60)
        label_12.place(x=630, y=60)
        label_1.place(x=750, y=60)
        label_2.place(x=860, y=60)
        label_3.place(x=990, y=60)
        label_4.place(x=1110, y=60)

        label_mon_1 = Label(screen_view, text=timetable[0][0], justify=CENTER, bg="light sky blue", width=15)
        label_mon_2 = Label(screen_view, text=timetable[0][1], justify=CENTER, bg="light sky blue", width=15)
        label_mon_3 = Label(screen_view, text=timetable[0][2], justify=CENTER, bg="light sky blue", width=15)
        label_mon_4 = Label(screen_view, text=timetable[0][3], justify=CENTER, bg="light sky blue", width=15)
        label_mon_5 = Label(screen_view, text=timetable[0][4], justify=CENTER, bg="light sky blue", width=15)
        label_mon_6 = Label(screen_view, text=timetable[0][5], justify=CENTER, bg="light sky blue", width=15)
        label_mon_7 = Label(screen_view, text=timetable[0][6], justify=CENTER, bg="light sky blue", width=15)
        label_mon_8 = Label(screen_view, text=timetable[0][7], justify=CENTER, bg="light sky blue", width=15)
        label_mon_9 = Label(screen_view, text=timetable[0][8], justify=CENTER, bg="light sky blue", width=15)

        label_mon_1.place(x=100, y=80)
        label_mon_2.place(x=220, y=80)
        label_mon_3.place(x=340, y=80)
        label_mon_4.place(x=460, y=80)
        label_mon_5.place(x=580, y=80)
        label_mon_6.place(x=700, y=80)
        label_mon_7.place(x=820, y=80)
        label_mon_8.place(x=940, y=80)
        label_mon_9.place(x=1060, y=80)

        label_tue_1 = Label(screen_view, text=timetable[1][0], justify=CENTER, bg="light sky blue", width=15)
        label_tue_2 = Label(screen_view, text=timetable[1][1], justify=CENTER, bg="light sky blue", width=15)
        label_tue_3 = Label(screen_view, text=timetable[1][2], justify=CENTER, bg="light sky blue", width=15)
        label_tue_4 = Label(screen_view, text=timetable[1][3], justify=CENTER, bg="light sky blue", width=15)
        label_tue_5 = Label(screen_view, text=timetable[1][4], justify=CENTER, bg="light sky blue", width=15)
        label_tue_6 = Label(screen_view, text=timetable[1][5], justify=CENTER, bg="light sky blue", width=15)
        label_tue_7 = Label(screen_view, text=timetable[1][6], justify=CENTER, bg="light sky blue", width=15)
        label_tue_8 = Label(screen_view, text=timetable[1][7], justify=CENTER, bg="light sky blue", width=15)
        label_tue_9 = Label(screen_view, text=timetable[1][8], justify=CENTER, bg="light sky blue", width=15)

        label_tue_1.place(x=100, y=160)
        label_tue_2.place(x=220, y=160)
        label_tue_3.place(x=340, y=160)
        label_tue_4.place(x=460, y=160)
        label_tue_5.place(x=580, y=160)
        label_tue_6.place(x=700, y=160)
        label_tue_7.place(x=820, y=160)
        label_tue_8.place(x=940, y=160)
        label_tue_9.place(x=1060, y=160)

        label_wed_1 = Label(screen_view, text=timetable[2][0], justify=CENTER, bg="light sky blue", width=15)
        label_wed_2 = Label(screen_view, text=timetable[2][1], justify=CENTER, bg="light sky blue", width=15)
        label_wed_3 = Label(screen_view, text=timetable[2][2], justify=CENTER, bg="light sky blue", width=15)
        label_wed_4 = Label(screen_view, text=timetable[2][3], justify=CENTER, bg="light sky blue", width=15)
        label_wed_5 = Label(screen_view, text=timetable[2][4], justify=CENTER, bg="light sky blue", width=15)
        label_wed_6 = Label(screen_view, text=timetable[2][5], justify=CENTER, bg="light sky blue", width=15)
        label_wed_7 = Label(screen_view, text=timetable[2][6], justify=CENTER, bg="light sky blue", width=15)
        label_wed_8 = Label(screen_view, text=timetable[2][7], justify=CENTER, bg="light sky blue", width=15)
        label_wed_9 = Label(screen_view, text=timetable[2][8], justify=CENTER, bg="light sky blue", width=15)

        label_wed_1.place(x=100, y=240)
        label_wed_2.place(x=220, y=240)
        label_wed_3.place(x=340, y=240)
        label_wed_4.place(x=460, y=240)
        label_wed_5.place(x=580, y=240)
        label_wed_6.place(x=700, y=240)
        label_wed_7.place(x=820, y=240)
        label_wed_8.place(x=940, y=240)
        label_wed_9.place(x=1060, y=240)

        label_thu_1 = Label(screen_view, text=timetable[3][0], justify=CENTER, bg="light sky blue", width=15)
        label_thu_2 = Label(screen_view, text=timetable[3][1], justify=CENTER, bg="light sky blue", width=15)
        label_thu_3 = Label(screen_view, text=timetable[3][2], justify=CENTER, bg="light sky blue", width=15)
        label_thu_4 = Label(screen_view, text=timetable[3][3], justify=CENTER, bg="light sky blue", width=15)
        label_thu_5 = Label(screen_view, text=timetable[3][4], justify=CENTER, bg="light sky blue", width=15)
        label_thu_6 = Label(screen_view, text=timetable[3][5], justify=CENTER, bg="light sky blue", width=15)
        label_thu_7 = Label(screen_view, text=timetable[3][6], justify=CENTER, bg="light sky blue", width=15)
        label_thu_8 = Label(screen_view, text=timetable[3][7], justify=CENTER, bg="light sky blue", width=15)
        label_thu_9 = Label(screen_view, text=timetable[3][8], justify=CENTER, bg="light sky blue", width=15)

        label_thu_1.place(x=100, y=320)
        label_thu_2.place(x=220, y=320)
        label_thu_3.place(x=340, y=320)
        label_thu_4.place(x=460, y=320)
        label_thu_5.place(x=580, y=320)
        label_thu_6.place(x=700, y=320)
        label_thu_7.place(x=820, y=320)
        label_thu_8.place(x=940, y=320)
        label_thu_9.place(x=1060, y=320)

        label_fri_1 = Label(screen_view, text=timetable[4][0], justify=CENTER, bg="light sky blue", width=15)
        label_fri_2 = Label(screen_view, text=timetable[4][1], justify=CENTER, bg="light sky blue", width=15)
        label_fri_3 = Label(screen_view, text=timetable[4][2], justify=CENTER, bg="light sky blue", width=15)
        label_fri_4 = Label(screen_view, text=timetable[4][3], justify=CENTER, bg="light sky blue", width=15)
        label_fri_5 = Label(screen_view, text=timetable[4][4], justify=CENTER, bg="light sky blue", width=15)
        label_fri_6 = Label(screen_view, text=timetable[4][5], justify=CENTER, bg="light sky blue", width=15)
        label_fri_7 = Label(screen_view, text=timetable[4][6], justify=CENTER, bg="light sky blue", width=15)
        label_fri_8 = Label(screen_view, text=timetable[4][7], justify=CENTER, bg="light sky blue", width=15)
        label_fri_9 = Label(screen_view, text=timetable[4][8], justify=CENTER, bg="light sky blue", width=15)

        label_fri_1.place(x=100, y=400)
        label_fri_2.place(x=220, y=400)
        label_fri_3.place(x=340, y=400)
        label_fri_4.place(x=460, y=400)
        label_fri_5.place(x=580, y=400)
        label_fri_6.place(x=700, y=400)
        label_fri_7.place(x=820, y=400)
        label_fri_8.place(x=940, y=400)
        label_fri_9.place(x=1060, y=400)





    view_option_button = Button(screen_view, text="View",width="10",bg="light sky blue")
    view_option_button.bind("<Button-1>",view_option_button_leftClick)
    view_option_button.place(x=100,y=474)


    def view_for_student_leftClick(event):
        timetable_file = open("timetable.txt", 'r')
        timetable_txt = timetable_file.readlines()
        timetable_file.close()

        timetable = []

        for each_line in timetable_txt:
            splitted_line = each_line.split()
            timetable.append(splitted_line)

        label_mon = Label(screen_view, text="Mon", justify=CENTER,bg="light sky blue")
        label_tue = Label(screen_view, text="Tue", justify=CENTER,bg="light sky blue")
        label_wed = Label(screen_view, text="Wed", justify=CENTER,bg="light sky blue")
        label_thu = Label(screen_view, text="Thu", justify=CENTER,bg="light sky blue")
        label_fri = Label(screen_view, text="Fri", justify=CENTER,bg="light sky blue")
        label_8 = Label(screen_view, text="8-9", justify=CENTER,bg="light sky blue")
        label_9 = Label(screen_view, text="9-10", justify=CENTER,bg="light sky blue")
        label_10 = Label(screen_view, text="10-11", justify=CENTER,bg="light sky blue")
        label_11 = Label(screen_view, text="11-12", justify=CENTER,bg="light sky blue")
        label_12 = Label(screen_view, text="12-1", justify=CENTER,bg="light sky blue")
        label_1 = Label(screen_view, text="1-2", justify=CENTER,bg="light sky blue")
        label_2 = Label(screen_view, text="2-3", justify=CENTER,bg="light sky blue")
        label_3 = Label(screen_view, text="3-4", justify=CENTER,bg="light sky blue")
        label_4 = Label(screen_view, text="4-5", justify=CENTER,bg="light sky blue")

        label_mon.place(x=10, y=80)
        label_tue.place(x=10, y=160)
        label_wed.place(x=10, y=240)
        label_thu.place(x=10, y=320)
        label_fri.place(x=10, y=400)
        label_8.place(x=150, y=60)
        label_9.place(x=270, y=60)
        label_10.place(x=390, y=60)
        label_11.place(x=510, y=60)
        label_12.place(x=630, y=60)
        label_1.place(x=750, y=60)
        label_2.place(x=860, y=60)
        label_3.place(x=990, y=60)
        label_4.place(x=1110, y=60)

        label_mon_1 = Label(screen_view, text=timetable[0][0], justify=CENTER, bg="light sky blue", width=15)
        label_mon_2 = Label(screen_view, text=timetable[0][1], justify=CENTER, bg="light sky blue", width=15)
        label_mon_3 = Label(screen_view, text=timetable[0][2], justify=CENTER, bg="light sky blue", width=15)
        label_mon_4 = Label(screen_view, text=timetable[0][3], justify=CENTER, bg="light sky blue", width=15)
        label_mon_5 = Label(screen_view, text=timetable[0][4], justify=CENTER, bg="light sky blue", width=15)
        label_mon_6 = Label(screen_view, text=timetable[0][5], justify=CENTER, bg="light sky blue", width=15)
        label_mon_7 = Label(screen_view, text=timetable[0][6], justify=CENTER, bg="light sky blue", width=15)
        label_mon_8 = Label(screen_view, text=timetable[0][7], justify=CENTER, bg="light sky blue", width=15)
        label_mon_9 = Label(screen_view, text=timetable[0][8], justify=CENTER, bg="light sky blue", width=15)

        label_mon_1.place(x=100, y=80)
        label_mon_2.place(x=220, y=80)
        label_mon_3.place(x=340, y=80)
        label_mon_4.place(x=460, y=80)
        label_mon_5.place(x=580, y=80)
        label_mon_6.place(x=700, y=80)
        label_mon_7.place(x=820, y=80)
        label_mon_8.place(x=940, y=80)
        label_mon_9.place(x=1060, y=80)

        label_tue_1 = Label(screen_view, text=timetable[1][0], justify=CENTER, bg="light sky blue", width=15)
        label_tue_2 = Label(screen_view, text=timetable[1][1], justify=CENTER, bg="light sky blue", width=15)
        label_tue_3 = Label(screen_view, text=timetable[1][2], justify=CENTER, bg="light sky blue", width=15)
        label_tue_4 = Label(screen_view, text=timetable[1][3], justify=CENTER, bg="light sky blue", width=15)
        label_tue_5 = Label(screen_view, text=timetable[1][4], justify=CENTER, bg="light sky blue", width=15)
        label_tue_6 = Label(screen_view, text=timetable[1][5], justify=CENTER, bg="light sky blue", width=15)
        label_tue_7 = Label(screen_view, text=timetable[1][6], justify=CENTER, bg="light sky blue", width=15)
        label_tue_8 = Label(screen_view, text=timetable[1][7], justify=CENTER, bg="light sky blue", width=15)
        label_tue_9 = Label(screen_view, text=timetable[1][8], justify=CENTER, bg="light sky blue", width=15)

        label_tue_1.place(x=100, y=160)
        label_tue_2.place(x=220, y=160)
        label_tue_3.place(x=340, y=160)
        label_tue_4.place(x=460, y=160)
        label_tue_5.place(x=580, y=160)
        label_tue_6.place(x=700, y=160)
        label_tue_7.place(x=820, y=160)
        label_tue_8.place(x=940, y=160)
        label_tue_9.place(x=1060, y=160)

        label_wed_1 = Label(screen_view, text=timetable[2][0], justify=CENTER, bg="light sky blue", width=15)
        label_wed_2 = Label(screen_view, text=timetable[2][1], justify=CENTER, bg="light sky blue", width=15)
        label_wed_3 = Label(screen_view, text=timetable[2][2], justify=CENTER, bg="light sky blue", width=15)
        label_wed_4 = Label(screen_view, text=timetable[2][3], justify=CENTER, bg="light sky blue", width=15)
        label_wed_5 = Label(screen_view, text=timetable[2][4], justify=CENTER, bg="light sky blue", width=15)
        label_wed_6 = Label(screen_view, text=timetable[2][5], justify=CENTER, bg="light sky blue", width=15)
        label_wed_7 = Label(screen_view, text=timetable[2][6], justify=CENTER, bg="light sky blue", width=15)
        label_wed_8 = Label(screen_view, text=timetable[2][7], justify=CENTER, bg="light sky blue", width=15)
        label_wed_9 = Label(screen_view, text=timetable[2][8], justify=CENTER, bg="light sky blue", width=15)

        label_wed_1.place(x=100, y=240)
        label_wed_2.place(x=220, y=240)
        label_wed_3.place(x=340, y=240)
        label_wed_4.place(x=460, y=240)
        label_wed_5.place(x=580, y=240)
        label_wed_6.place(x=700, y=240)
        label_wed_7.place(x=820, y=240)
        label_wed_8.place(x=940, y=240)
        label_wed_9.place(x=1060, y=240)

        label_thu_1 = Label(screen_view, text=timetable[3][0], justify=CENTER, bg="light sky blue", width=15)
        label_thu_2 = Label(screen_view, text=timetable[3][1], justify=CENTER, bg="light sky blue", width=15)
        label_thu_3 = Label(screen_view, text=timetable[3][2], justify=CENTER, bg="light sky blue", width=15)
        label_thu_4 = Label(screen_view, text=timetable[3][3], justify=CENTER, bg="light sky blue", width=15)
        label_thu_5 = Label(screen_view, text=timetable[3][4], justify=CENTER, bg="light sky blue", width=15)
        label_thu_6 = Label(screen_view, text=timetable[3][5], justify=CENTER, bg="light sky blue", width=15)
        label_thu_7 = Label(screen_view, text=timetable[3][6], justify=CENTER, bg="light sky blue", width=15)
        label_thu_8 = Label(screen_view, text=timetable[3][7], justify=CENTER, bg="light sky blue", width=15)
        label_thu_9 = Label(screen_view, text=timetable[3][8], justify=CENTER, bg="light sky blue", width=15)

        label_thu_1.place(x=100, y=320)
        label_thu_2.place(x=220, y=320)
        label_thu_3.place(x=340, y=320)
        label_thu_4.place(x=460, y=320)
        label_thu_5.place(x=580, y=320)
        label_thu_6.place(x=700, y=320)
        label_thu_7.place(x=820, y=320)
        label_thu_8.place(x=940, y=320)
        label_thu_9.place(x=1060, y=320)

        label_fri_1 = Label(screen_view, text=timetable[4][0], justify=CENTER, bg="light sky blue", width=15)
        label_fri_2 = Label(screen_view, text=timetable[4][1], justify=CENTER, bg="light sky blue", width=15)
        label_fri_3 = Label(screen_view, text=timetable[4][2], justify=CENTER, bg="light sky blue", width=15)
        label_fri_4 = Label(screen_view, text=timetable[4][3], justify=CENTER, bg="light sky blue", width=15)
        label_fri_5 = Label(screen_view, text=timetable[4][4], justify=CENTER, bg="light sky blue", width=15)
        label_fri_6 = Label(screen_view, text=timetable[4][5], justify=CENTER, bg="light sky blue", width=15)
        label_fri_7 = Label(screen_view, text=timetable[4][6], justify=CENTER, bg="light sky blue", width=15)
        label_fri_8 = Label(screen_view, text=timetable[4][7], justify=CENTER, bg="light sky blue", width=15)
        label_fri_9 = Label(screen_view, text=timetable[4][8], justify=CENTER, bg="light sky blue", width=15)

        label_fri_1.place(x=100, y=400)
        label_fri_2.place(x=220, y=400)
        label_fri_3.place(x=340, y=400)
        label_fri_4.place(x=460, y=400)
        label_fri_5.place(x=580, y=400)
        label_fri_6.place(x=700, y=400)
        label_fri_7.place(x=820, y=400)
        label_fri_8.place(x=940, y=400)
        label_fri_9.place(x=1060, y=400)

    view_student_button = Button(screen_view,text="View for Student",bg="light sky blue")
    view_student_button.bind("<Button-1>",view_for_student_leftClick)
    view_student_button.place(x=500,y=474)

    def main2_leftClick(event):
        screen_view.destroy()
        main_2_screen()
    main_menu_button = Button(screen_view,text="Main Menu",bg="light sky blue")
    main_menu_button.bind("<Button-1>",main2_leftClick)
    main_menu_button.place(x=1100,y=474)

    screen_view.mainloop()




timetable_file = open("timetable.txt", 'r')
timetable_txt = timetable_file.readlines()
timetable_file.close()
if timetable_txt == []:
    main_screen()
else:
    main_2_screen()


