import re

print("Magical Calculartor")


run = True
previous = 0

def matah_function():
    global previous
    global run
    equation = ""




    if previous == 0:
        equation = input("Enter The Equation ")

    else:
        equation = input(str(previous))




    if equation=='quit':
        run = False
        print("Good Bye")

    else:
        equation = re.sub('[a-zA-z,.():;]','',equation)


        if previous==0:
            previous = str(eval(equation))
            print("You typed : " + previous)
        else:
            previous = str(eval(previous+equation))
            print("You typed"+previous)






while run:
    matah_function()

