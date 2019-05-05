# hm.py
# Yanilda
# 5.5.19
# solution to homework recap
import math

def sphereArae( radius ):
    '''
        Returns the surface area of a sphere having the given radius
    '''
    return 4*math.pi*radius**2

def sphereVolume( radius ):
    '''
        Returns the volume of a sphere having the given radius
    '''
    return 4/3*math.pi*radius**3

def sumN( n ):
    '''
        Returns the sum of the n natural numbers
    '''
    total=0
    for i in range(1,n+1):
        total += i
    return total
def toNumbers( strList ):
    '''
        strList is a list of strings, each which represents a number.
        Modify each entry in the list by converting it into a number
    '''
    for i in range(len(strList)):
        strList[i] = int( strList[i] )
    

def sumSquares( n ):
    total=0
    for i in range(1,n+1):
        total += i**2
    return total

def sumListSquare(list2=[]):
    total = 0
    for numbers in list2:
        total += numbers**2
    return total
    
def readNumbers():
    print("Welcome\nThis program read numbers from file and calculate the sum of squares")
    filename   = input("Enter the name of the file: ")
    infile     = open(filename, "r")

    lines      = infile.readlines();# print(lines)
    toNumbers( lines ) ;# print(lines)
    total      = sumListSquare( lines )
    
    infile.    close()
    print(total, "is the sum of the square of every value in your file")

