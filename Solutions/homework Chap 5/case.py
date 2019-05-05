#case.py
#Yanilda
#5.5.19
#Contains a function that prints out the all upper case version of all letters in  a string

def lower2Upper(word):
     newWord=""
     
     for letter in word:
         numericValue=ord(letter)
         if  97<= numericValue <=122:
             newWord += chr(numericValue-32)
         else:
             newWord += letter
             
     print(newWord)
