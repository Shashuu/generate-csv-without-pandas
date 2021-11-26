#!/usr/bin/env python3

# Template for midterm

def in_parens(s):
    # function that gets text froma string between a set of parentheses.
    #   Example "Hi (Bob)" yields "Bob"
    #
    # YOU COMPLETE THIS
    #
    return(s[s.find('(')+1:s.find(')')])

def letter_grade(score):
    # function to convert a floating point decimal percentage score into a letter grade
    score=in_parens(score)
    score=float(score[:-1])
    
    if score >= 97:
        return "A+"
    if score >= 93:
        return "A"
    if score >= 90:
        return "A-"
    if score >= 87:
        return "B+"
    if score >= 83:
        return "B"
    if score >= 80:
        return "B-"
    if score >= 77:
        return "C+"
    if score >= 73:
        return "C"
    if score >= 70:
        return "C-"
    if score >= 67:
        return "D+"
    if score >= 63:
        return "D"
    if score >= 60:
        return "D-"

    #
    # COMPLETE THIS
    #

    return "F"

def parse_data(data):
    # function to parse the file data into the data structure fo your choosing.

    sep1 = "============================================================\n"
    sep2 = "------------------------------------------------------------\n"
    avg=[]

    students = [] # example
    with open(data, 'r') as fh:
        l=[]
        header=[]
        for i in fh.readlines():
            #print(i)
            if i[:2]=='cs':
                #print(1)
                t=i.split(" ")
                l.append(t[-2][:-1])
                l.append(t[-1][:-1])
                #break
                l.append(t[0][:5])
                l.append(t[0])
            elif i[0]==' ' and '/' not in i:
                #print(2)
                t=i.split(" ")
                l.append(t[-1].split("@")[0])
            elif i==sep2:
                #print(3)
                continue
            elif ':' in i:
                if i[:-2] not in header:
                    header.append(i[:-2])
                if 'final' in i or 'mid' in i:
                    final_set=1
                #print(4)
                continue
            elif '/' in i:
                #print(5)
                if final_set:
                    avg.append(float(in_parens(i)[:-1]))
                    if len(avg)==2:
                        print(str((avg[0]+avg[1])/2)+'%')
                        l.append(letter_grade(str((avg[0]+avg[1])/2)+'%'))
                        avg=[]
                        final_set=0
                else:
                    l.append(letter_grade(i))
            elif i==sep1:
                #print(6)
                students.append(l)
                l=[]

    print(students)
    #print(to_csv(students, data))
    #
    # COMPLETE THIS
    header=['last_name', 'first_name', 'username', 'course', 'cs_account']+header
    new_name=data[:-4]+'1.csv'
    #header=['last_name', 'first_name', 'username', 'course', 'cs_account', 'final', 'lab1', 'lab2', 'lab3', 'lab4', 'lab5', 'lab6', 'midterm', 'quiz1', 'quiz2', 'quiz3', 'quiz4']
    #
    with open(new_name, 'w') as op:
        op.write("%s"%(','.join(header)))
        op.write("\n")
        for i in students:
            op.write("%s"%(','.join(i)))
            op.write("\n")

    return new_name

parse_data('cs002.txt')

def to_csv(students, data):
    # function to create a CSV file from the your data structure, with the
    #   field separator as the comma, and the record separator as the newline

    #
    # COMPLETE THIS
    

    return csv_as_str


if __name__ == "__main__":

    print(f'Running file "{__file__}..."')

    # Read in each file from the folder `data` and convert it into a CSV format.
    #   The expected outputs are given so that you may check your work.

    #
    # COMPLETE THIS
    #
