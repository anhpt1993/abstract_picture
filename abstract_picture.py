# abstract pictures
import turtle as t
import random

def get_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

def draw_rectangle(width, height, color):
    t.pendown()
    t.pencolor(color)
    for i in range(4):
        if i % 2 == 0:
            t.forward(width)
        else:
            t.forward(height)
        t.right(90)
    t.penup()

def draw_circle(radius, color):
    t.pendown()
    t.pencolor(color)
    t.circle(radius)
    t.penup()

def draw_ellipse(radius, color):
    t.pendown()
    t.pencolor(color)
    for i in range(2):
        t.circle(radius, 90)
        t.circle(radius / 2, 90)
    t.penup()

def draw_pentagon(d, color):
    t.pendown()
    t.pencolor(color)
    for i in range(5):
        t.forward(d)
        t.left(72)
    t.penup()

def draw_square(d, color):
    t.pendown()
    t.pencolor(color)
    for i in range(4):
        t.forward(d)
        t.right(90)
    t.penup()

def draw_equilateral_triangle(d, color):
    t.pendown()
    t.pencolor(color)
    for i in range(3):
        t.forward(d)
        t.left(120)
    t.penup()

def input_data():
    while True:
        try:
            number = int(input())
            if number > 0:
                return number
                break
            else:
                print("Input a positive number. Try again``\n")
        except ValueError:
            print("Invalid input. Try again\n")

def input_picture():
    print("How many pictures do you want to draw: ", end = "\t")
    return input_data()

def choose_option():
    print("Please choose your option: ")
    print("""
    1. Rectangle
    2. Square
    3. Circle
    4. Equilateral Triangle
    5. Ellipse
    6. Pentagon\n""")
    while True:
        try:
            option = (int(input("Your choice: ")))
            if 1 <= option <= 6:
                return option
                break
            else:
                print("You only have 6 options to choose. Try again\n")
        except ValueError:
            print("Invalid input. Try again\n")

def loop_rectangle(func, number):
    for i in range(number):
        func(width, height, get_color())
        t.right(360/number)

def loop_other(func, number):
    for i in range(number):
        func(distance, get_color())
        t.right(360/number)

def try_again():
    choice = input("Do you want to try again? (Y/N): ").upper().strip()
    if choice == "Y" or choice == "YES":
        return True
    else:
        print("Bye! See you next time!!!")
        exit()

if __name__ == '__main__':

    while True:
        option = choose_option()
        number = input_picture()

        t.pensize(3)
        t.pendown()
        t.speed(1000)
        t.colormode(255)

        if option == 1:
            print("Width: ", end = "\t")
            width = input_data()
            print("Height: ", end = "\t")
            height = input_data()
            loop_rectangle(draw_rectangle, number)
        elif option == 2:
            print("Side: ", end = "\t")
            distance = input_data()
            loop_other(draw_square, number)
        elif option == 3:
            print("Radius: ", end="\t")
            distance = input_data()
            loop_other(draw_circle, number)
        elif option == 4:
            print("Side: ", end="\t")
            distance = input_data()
            loop_other(draw_equilateral_triangle, number)
        elif option == 5:
            print("Radius: ", end="\t")
            distance = input_data()
            loop_other(draw_ellipse, number)
        else:
            print("Side: ", end="\t")
            distance = input_data()
            loop_other(draw_pentagon, number)

            t.right(360/number)

        t.resetscreen()
        try_again()