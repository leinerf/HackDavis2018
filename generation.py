from random import *
import itertools

def generate(problemNumber):
    p= open("Problems.txt","w+")
    a= open("Answers.txt","w+")
    for j in range(0, problemNumber):
        argNumber = randint(2,4)
        s = ""
        k = ""
        answer = 0
        for i in range(0, argNumber+1):
            operand = randint(1,15)
            if i == 0:
                answer = operand
            opearator = randint(0,2)
            s += str(operand)
            if i == argNumber-1:
                answer = eval(s)
                s += " =__\n"
                a.write(str(j+1) + ". " + str(answer) +"\n")
                break
            if opearator == 0:
                s+= " + "
            if opearator == 1:
                s+= " * "
            if opearator == 2:
                s+= " - "
        p.write(s)
    p.close()
    a.close()
    #for i in range(0,problemNumber):
    #    a = randint(1,20)
    #    b = randint(1,20)
    #    s = str(a) + " * " + str(b) + " =__\n"
    #    f.write(s)
generate(10)