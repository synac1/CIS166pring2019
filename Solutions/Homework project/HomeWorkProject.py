'''
    file   : HomeWorkProject.py
    @Author: Yanilda
    Created: 5.4.19
    Desc   : Solution to the Homework Project
'''


#Chap2
# 1
#Modify convert.py to print an introduction
def convert():
    print("Welcome to temperature convertor")
    print("This Program will convert from  celsius to farenheit")
    
    celsius= eval(input("What is the celsius temperature? "))
    farenheit = 9/5 * celsius +32
    
    print("The temperature is", farenheit, "degrees farenheit.")
# 3
#Modify convert.py to execute 5 times before quitting
def convert2():
    for i in range(5):
        celsius= eval(input("What is the celsius temperature? "))
        farenheit = 9/5 * celsius +32
        print("The temperature is", farenheit, "degrees farenheit.")
    print("Done")


# 9
#Write a program that converts distance in kilometers to miles, 1 km= 0.62 miles
def km2miles():
    print("Welcome to km2miles")
    print("This Program will convert from km to miles")
    km= eval(input("Please Enter distance in kilometers: "))
    miles= km * 0.62
    print("The distance is", miles,"miles")

#11
#Write an interactive calculator, where the user enters math expression
def calculator():
    print("Welcome to Interactive Calculator")
    
    for i in range(5):
        mathExpression = eval(input("Enter expression:"))
        print("Result:", mathExpression)
        

#chap3
import math
#1
#calculate the volume and surface area of sphere
def sphereAreaVolume():
    print("Welcome to sphereAreaVolume ")
    print("This function will calculate the sphere volume and area")
    radius = eval(input("Please enter radius: "))
    
    volume = 4/3 *  math.pi * radius**3
    area   = 4/3 *  math.pi * radius**2
    
    print("The sphere has an area of", area, "and a volume of", volume)
#2
#calculate the cost per square inch of a circular pizza, given its diameter and price. A= pi*r**2
def costOfPizza():
    print("This function calculates the cost per square inch of a pizza")
    diameter, price=eval(input("Pleasea enter diameter and price separated by comma: "))
    
    radius = diameter/2
    area   = math.pi*radius**2
    cost   = price/area
    
    print("The cost per square inch is",cost)
#3
#Determine the molecular weight of a hydeocarbon based on the number of hydrogen, carbon, and oxygen atoms
# h= 1.0079 grams/mole, c=12.011, o=15.9994
def weight():
    print("Welcome, this function will calculate the molecular weight:")
    hydrogen = int(input("Enter number of hydrogen atoms:"))
    carbon   = int(input("Enter number of carbon atoms  :"))
    oxygen   = int(input("Enter number of oxygen atoms  :"))

    hydrogen *=  1.0079
    carbon   *=  12.011
    oxygen   *=  15.9994

    print("\t____Weight___\nHydrogen:\t%10.2fgm/mol\nCarbon  :\t%10.2fgm/mol\nOxygen  :\t%10.2fgm/mol"%(hydrogen, carbon, oxygen))

#12
#Find the sum of the cubes of the first n natural numbers: n is provided by the user
def sumCube():
    print("Welcome this program will calculate the sum of cube of the first n natural numbers")
    n=int(input("Enter a number as the limit:"))

    total=0
    for i  in range(n+1):
        total += i**3
    print("The sum of the first %dth natural numbers is %d"%(n,total))
    

#13
#sum of series of numbers entered by the user, ask user how many numbers to add
def sumSeries():
    print("Welcome, this program will sum a series of numbers entered by the user")
    n=int(input("How many numbers do you want to add? "))

    total=0
    for i in range(n):
        total += eval(input("Enter a number: "))

    print("The result is:", total)
#14
#Average of series of numbers entered by the user, ask user how mant numbers to add
def averageSeries():
    print("Welcome, this function will average a series of numbers entered by the user")
    n=int(input("How many numbers do you want to submit? "))

    total = 0.0
    for i in range(n):
        total += eval(input("Enter a number: "))
        
    total /=n
    print("The result is:", total)
#16
    #Computes the nth fib number
def fibonacci():
    print("Welcome, This function computes nth fib number ")
    n=int(input("Enter a number: "))
    fib=0
    num1=0
    num2=1
    for i in range(1, n):
        fib  = num1 + num2 
        num1 = num2
        num2 = fib
    print("%dth fibonacci is: %d"%(n,fib))
####
###### Chapter 4
from graphics import *
#1 draw squares
def drawSquares():
    win  = GraphWin("drawSquares",400, 400)

    for i in range(10):
        p1 = win.getMouse()
        p2 = win.getMouse()
        rec= Rectangle(p1,p2)
        rec.setFill("blue")
        rec.draw(win)
    print("Click again to quit")
    
    win.getMouse()
    win.close()
    
#2 Archery Target
def archeryTarget():
    win           = GraphWin("Target",400, 600)
    center        = Point(200,300)
    radius        = 50
    yellow_circle = Circle(center, radius)
    red_circle    = Circle(center, radius*2)
    blue_circle   = Circle(center, radius*3)
    white_circle  = Circle(center, radius*4)

    yellow_circle.setFill("yellow")
    red_circle.   setFill("red")
    blue_circle.  setFill("blue")
    white_circle. setFill("white")

    white_circle. draw(win)
    blue_circle.  draw(win)
    red_circle.   draw(win)
    yellow_circle.draw(win)
    win.getMouse()
    win.close()
    
# 3 draw a face
def face():
    win       = GraphWin("Face", 500,500)
    
    circle    = Circle (Point(250, 250),250)
    left_eye  = Line   (Point(200,50), Point(200, 150))
    right_eye = Line   (Point(300,50), Point(300, 150))
    mouth     = Line   (Point(200,350), Point(300,350))

    circle.   setFill("beige")
    left_eye. setFill("brown")
    right_eye.setFill("brown")
    mouth.    setFill("red")

    left_eye. setWidth(15)
    right_eye.setWidth(15)
    mouth.    setWidth(10)
    
    circle.   draw(win)
    left_eye. draw(win)
    right_eye.draw(win)
    mouth.    draw(win)
    
    win.getMouse()
    win.close()


#4 Draw a winter scene with christmas tree and snowman
def winter():
    win         = GraphWin("Winter", 600,600)
    win.        setBackground("skyblue")

    ground      = Rectangle(Point(0,300), Point(600,600))
    first_ball  = Circle(Point(110,350),100)
    second_ball = Circle(Point(110,270),75)
    last_ball   = Circle(Point(110,200), 50)
    stem        = Rectangle(Point(450,350),Point(500,300))
    leaves      = Polygon(Point(475,50),Point(400,310),Point(550,310))
    
    
    ground.     setFill("white")
    first_ball. setFill("white")
    second_ball.setFill("white")
    last_ball.  setFill("white")
    stem.       setFill("tan")
    leaves.     setFill("green")

    ground.     draw(win)
    first_ball. draw(win)
    second_ball.draw(win)
    last_ball.  draw(win)
    stem.       draw(win)
    leaves.     draw(win)
    win.getMouse()
    win.close()
#7 Circle intersection, set Coords from -10,-10 to 10,10
def intersection():
    print("Welcome\nThis function will display a circle at the center and given radius, and y-intercept")
    radius = float(input("Please enter radius (0 to 10): "))
    yint   = float(input("Please enter y-intercept (-10 to 10) yint <= radius: "))

    x1     = math.sqrt(radius**2 - yint**2)
    x2     = -x1
    print("x1:%.3f, x2:%.3f"%(x1,x2))
    
    win    = GraphWin("Circle Intersection", 400, 400)
    win.   setCoords(-10,-10,10,10)

    circle = Circle(Point(0,0), radius)
    p1     = Point (x1, yint)
    p2     = Point (x2, yint)
    line   = Line  (Point(-10,yint),Point(10,yint))

    circle.setFill("white")
    p1.    setFill("red")
    p2.    setFill("red")

    circle.draw(win)
    line.draw(win)
    p1.draw(win)
    p2.draw(win)

#10 Triangle Information
def triangleInfo():
    win       = GraphWin("TriangleInfo", 500,500)
    win.      setCoords(-10,-10,10,10)

    label1    = Text(Point(0,8), "Click to create a triangle")
    label1.   draw(win)
    point1    = win.getMouse()
    point2    = win.getMouse()
    point3    = win.getMouse()
    triangle  = Polygon(point1, point2, point3)
    
    a         = (point2.getY()- point1.getY())**2 + (point2.getX()- point1.getX())**2
    b         = (point3.getY()- point2.getY())**2 + (point3.getX()- point2.getX())**2
    c         = (point1.getY()- point3.getY())**2 + (point1.getX()- point3.getX())**2
    perimeter = a+b+c
    s         = perimeter/2
    area      = math.sqrt(s*(s-a)*(s-b)*(s-c))
    
    triangle. draw(win)
    print("Area is %.3f\nPerimeter is %.3f"%(area, perimeter))
    win.getMouse()
    win.close()
    

#11 Five Click House
def fiveClickHome():

    win         = GraphWin("five click home", 500,500)
    
    label       = Text(Point( 250,10),"Click to draw a house")
    label.      draw(win)

    point1      = win.getMouse()
    point2      = win.getMouse()
    wall        = Rectangle(point1, point2)
    wall.       draw(win)
    
    point3      = win.getMouse()
    #point3 for door, center top, door width 1/5 of wall
    frameWidth  = point2.getX()-point1.getX()
    door        = Rectangle(Point(point3.getX()-(frameWidth/10), point3.getY()), Point(point3.getX()+(frameWidth/10), point1.getY()))
    door.       draw(win)
    
    point4      = win.getMouse()
    ##Center of a square window half wide as the door
    doorWidth   = door.getP2().getX()-door.getP1().getX()
    window      = Rectangle(Point(point4.getX()-(doorWidth/4), point4.getY()-(doorWidth/4)),Point(point4.getX()+(doorWidth/4), point4.getY()+(doorWidth/4)))
    window.     draw(win)
    
    point5      = win.getMouse()
    roof        = Polygon(point5, point2, Point(point1.getX(),point2.getY()))
    roof.       draw(win)
    win.getMouse()
    win.close()
#currencyConverter()
#   A function that converts from Argentine Peso to USD and Euros
def currencyConverter():
    print("Welcome to currency converter\nfrom Argentine Peso To Euro and USD\n")

    peso   = eval(input("Enter amount in Argentine Pesos: "))
    
    euro   = peso*0.020
    dollar = peso*0.022

    print("%.2f pesos:\n%.2f euros \n%.2f usd"%(peso, euro, dollar))


    

    
    


    





