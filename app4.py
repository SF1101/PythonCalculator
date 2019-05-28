import sys
import time
t = int(5)
answer = input("Calculator!\n Press \"Enter\" to continue! ")

while answer != "No":
    num1 = float(input("Enter a number: "))
    num2 = float(input("Enter another number: "))
    add = num1+num2
    subtract = float(num1)-float(num2)
    multiply = float(num1)*float(num2)
    divide = float(num1)/float(num2)
    function = input("Enter a math function: \n Add/Subtract/Multiply/Divide\n")

    if function == "Add":
        print(add)
    if function == "Subtract":
        print(subtract)
    if function == "Multiply":
        print(multiply)
    if function == "Divide":
        print(divide)
    answer = input("Do you want to continue? Yes/No?\n")
    if answer == "No":
        print("See you later! :) \nExiting in...")
        for i in range(2, 0, -1):
            sys.stdout.write(str(i) + ' seconds\n')

            sys.stdout.flush()
            time.sleep(2)
        print("Bye!")
        time.sleep(0.5)



        break
