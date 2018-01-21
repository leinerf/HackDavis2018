from random import *
import itertools

def generateDict(problemNumber):
#    p= open("Problems.txt","w+")
#    a= open("Answers.txt","w+")
    problemList = []
    for j in range(0, problemNumber):
        problems = {}
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
                problems["leftHand"] = s
                problems["rightHand"] = answer
                problemList.append(problems)
  #              a.write(str(j+1) + ". " + str(answer) +"\n")
                break
            if opearator == 0:
                s+= " + "
            if opearator == 1:
                s+= " * "
            if opearator == 2:
                s+= " - "
    return problemList
 #       p.write(s)
        
 #   p.close()
 #   a.close()
    #for i in range(0,problemNumber):
    #    a = randint(1,20)
    #    b = randint(1,20)
    #    s = str(a) + " * " + str(b) + " =__\n"
    #    f.write(s)

